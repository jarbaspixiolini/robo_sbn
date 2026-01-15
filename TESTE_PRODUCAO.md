# 🧪 Checklist: Teste do Robô em Produção

Data: January 15, 2026  
Status: **PRONTO PARA TESTE**

---

## ✅ Pré-requisitos (O que você TEM agora)

- ✅ Código do monitor completo (run.py, collectors, storage, alerts)
- ✅ Banco de dados SQLite estruturado (3 tabelas: serp_runs, play_runs, seen_domains)
- ✅ Integração Slack configurada (webhook ativo)
- ✅ Config.yaml com 5 keywords + 7 cidades + 2 devices
- ✅ Variável de ambiente SLACK_WEBHOOK_URL no .env
- ✅ Testes unitários passando (test_monitor.py: 5/5 ✅)
- ✅ GitHub Actions workflow criado (cron: seg/qua/sex 14:00 UTC)

---

## ⚠️ Bloqueadores Conhecidos

| Item | Status | Solução |
|------|--------|---------|
| **Playwright browsers** | ❌ Bloqueado | SSL cert error (corporate proxy) |
| **Google APIs** | ❌ Não testado | Precisa GOOGLE_SERP_API_KEY + GOOGLE_SEARCH_ENGINE_ID |
| **Real SERP data** | ❌ Bloqueado | Depende de Playwright |
| **Real Play data** | ❌ Bloqueado | Depende de Playwright |

---

## 📋 O Que Precisa Para Teste em Produção

### **Fase 1: Validação Local (30 min) — FAÇA AGORA**

```powershell
# 1. Ativar virtual environment
cd c:\Users\jarbas.pixiolini\Downloads\robo_sbn\conexa-monitor
.\venv_novo\Scripts\Activate.ps1

# 2. Rodar testes (sem Playwright)
python test_monitor.py

# 3. Validar variáveis de ambiente
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('SLACK_WEBHOOK_URL:', os.getenv('SLACK_WEBHOOK_URL'))"

# 4. Validar config.yaml
python -c "import yaml; print(yaml.safe_load(open('config.yaml')))"

# 5. Validar database schema
python -c "from storage.db import init_db; init_db(); print('✅ Database OK')"
```

---

### **Fase 2: Resolver Google APIs (1-2h) — NECESÁRIO**

#### **Opção A: Usar SerpAPI (Recomendado - Rápido)**

```bash
# 1. Criar conta em https://serpapi.com (free tier: 100 buscas/mês)
# 2. Copiar API key
# 3. Atualizar .env

GOOGLE_SERP_API_KEY=seu_serpapi_key_aqui
GOOGLE_SEARCH_ENGINE_ID=ignorar_para_serpapi
```

**Modificação necessária em collectors/google_serp.py:**
```python
# Mudar de Playwright para requests + SerpAPI
import requests

async def collect_serp(config: dict, browser=None):
    """Collect SERP data using SerpAPI instead of Playwright"""
    api_key = config.get('google_serp', {}).get('api_key')
    
    for keyword in config.get('keywords', []):
        response = requests.get(
            'https://serpapi.com/search',
            params={'q': keyword, 'api_key': api_key, 'location': 'Brazil', 'num': 30}
        )
        # Process response...
```

#### **Opção B: Resolver SSL Certificate (Difícil)**

Se quiser manter Playwright:
1. Contatar IT para whitelist: `playwright.dev`, `download.pytorch.org`
2. Ou configurar proxy em PowerShell:
```powershell
$env:HTTPS_PROXY = "http://seu-proxy:porta"
$env:HTTP_PROXY = "http://seu-proxy:porta"
playwright install chromium
```

---

### **Fase 3: Teste Sem Playwright (Agora) — IMEDIATO**

**Você pode testar TUDO EXCETO coleta de dados:**

```powershell
# 1. Testar database
python -c "
from storage.db import init_db, conn
init_db()
c = conn()
print(c.execute('SELECT COUNT(*) FROM serp_runs').fetchone())
print('✅ Database working')
"

# 2. Testar Slack integration
python -c "
from alerts.slack import send_slack
import os
from dotenv import load_dotenv

load_dotenv()
webhook = os.getenv('SLACK_WEBHOOK_URL')
send_slack('Test message', webhook)
print('✅ Slack integration working')
"

# 3. Testar config loading
python -c "
from run import load_config
config = load_config()
print('Keywords:', config['keywords'])
print('Cities:', len(config['capitals_sul_sudeste']))
print('✅ Config loading working')
"
```

---

### **Fase 4: Teste em Produção com Mock Data (1h) — RECOMENDADO**

**Criar teste com dados simulados (sem Playwright):**

```powershell
# Criar arquivo: test_production.py

python -c "
import asyncio
from datetime import datetime, timezone
from storage.db import init_db, conn
from alerts.slack import send_slack
import os
from dotenv import load_dotenv

async def test_production():
    load_dotenv()
    init_db()
    
    # Insert mock SERP data
    ts = datetime.now(timezone.utc).isoformat()
    with conn() as c:
        c.execute('''
            INSERT INTO serp_runs (ts, keyword, city, uf, device, has_ads, domains)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ts, 'conexa', 'São Paulo', 'SP', 'mobile', 1, '{}'))
        c.commit()
    
    # Test Slack alert
    webhook = os.getenv('SLACK_WEBHOOK_URL')
    send_slack('🧪 Teste de produção: Sistema funcionando!', webhook)
    print('✅ Production test passed')

asyncio.run(test_production())
"
```

---

### **Fase 5: Deploy em Produção (GitHub Actions) — PRÓXIMO**

**Pré-requisitos:**
- ✅ GOOGLE_SERP_API_KEY configurado (ou SerpAPI)
- ✅ SLACK_WEBHOOK_URL ativo no GitHub Secrets
- ✅ Playwright bloqueado OU resolvido

**Próximos passos:**
1. Editar `.github/workflows/competitor-monitor.yml`
2. Remover `playwright install` se usar SerpAPI
3. Adicionar error handling para Playwright
4. Push para GitHub
5. Ir em Actions → Run workflow manualmente

---

## 🎯 Recomendação

### **Caminho Mais Rápido (próximas 2h):**

1. **Agora:** Rodar Fase 1 (validação local)
2. **Próximos 20 min:** Escolher Opção A (SerpAPI) — mais fácil
3. **Próxima hora:** Modificar `google_serp.py` para usar SerpAPI
4. **Última hora:** Rodar Fase 4 (teste de produção com mock)
5. **Resultado:** Sistema pronto para GitHub Actions

---

## 📊 Métricas de Teste

Esperado após teste bem-sucedido:

```
✅ Database: 3 tabelas + esquema validado
✅ Slack: 1 mensagem de teste recebida
✅ Config: 5 keywords + 7 cidades carregadas
✅ Mock data: 10 registros inseridos no DB
✅ GitHub Actions: Workflow pronto (trigger manual)
```

---

## ❓ Dúvidas Frequentes

**P: Posso testar sem resolver Google APIs?**  
R: Sim, mas só database + Slack. Nenhuma coleta real de dados.

**P: SerpAPI é melhor que Playwright?**  
R: Para este caso: SIM. Mais rápido, mais confiável, sem SSL issues.

**P: Quanto custa SerpAPI?**  
R: Free tier = 100 buscas/mês. Pago = $50/mês para 10k buscas.

**P: Posso rodar localmente sem GitHub Actions?**  
R: Sim, rodar `python run.py` direto na sua máquina.

