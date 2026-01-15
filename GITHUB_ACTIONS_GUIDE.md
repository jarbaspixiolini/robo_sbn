# 🚀 Guia: Testar GitHub Actions Workflow

## Passo 1: Adicionar Secrets no GitHub (IMPORTANTE!)

Sem os secrets, o workflow vai falhar. Siga exatamente:

### 1.1 Ir para Settings de Secrets

1. Abra: https://github.com/jarbas-pixiolini/robo_sbn
2. Clique em: **Settings** (no topo direito)
3. Clique em: **Secrets and variables** (na esquerda)
4. Clique em: **Actions** (abaixo de Secrets and variables)

### 1.2 Adicionar SERPAPI_API_KEY

1. Clique em: **New repository secret**
2. Name: `SERPAPI_API_KEY`
3. Secret: `3f70e47910d8b5833d3c915284949211966fb0a0d97738a1698bce035a671768`
4. Clique em: **Add secret**

### 1.3 Adicionar SLACK_WEBHOOK_URL

1. Clique em: **New repository secret** (novamente)
2. Name: `SLACK_WEBHOOK_URL`
3. Secret: `https://hooks.slack.com/triggers/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`
4. Clique em: **Add secret**

Resultado esperado: 2 secrets criados com checkmark verde ✓

---

## Passo 2: Ir para Actions

1. Abra: https://github.com/jarbas-pixiolini/robo_sbn
2. Clique em: **Actions** (no topo)
3. Você verá na esquerda: **Conexa Monitor - Competitor Intelligence**

---

## Passo 3: Disparar Workflow Manualmente

1. Clique em: **Conexa Monitor - Competitor Intelligence** (na esquerda)
2. Clique em: **Run workflow** (botão azul)
3. Mantém **branch: main** selecionado
4. Clique em: **Run workflow** (no dropdown)

Resultado esperado: Workflow inicia com status "running"

---

## Passo 4: Acompanhar Execução

1. Você verá a execução em tempo real com status
2. Tempo estimado: 2-3 minutos

### Durante a execução:

- 🟡 **Yellow** = Executando
- 🟢 **Green** = Sucesso ✓
- 🔴 **Red** = Erro ❌

### Passos do workflow:

1. ✓ Checkout code (rápido)
2. ✓ Set up Python 3.11 (rápido)
3. ✓ Cache pip packages (rápido)
4. ✓ Install dependencies (30 seg)
5. ✓ Run Conexa Monitor (40-50 seg)
6. ✓ Upload artifacts (rápido)
7. ✓ Commit database changes (rápido)

---

## Passo 5: Ver Resultados

### Se tudo OK (🟢 Green):

1. Clique no job **monitor** 
2. Você verá:
   - ✓ All steps passed
   - [OK] SERP buscas: 70
   - [OK] Novos dominios detectados: X
   - [OK] Monitoramento concluído!

3. Você receberá alerta no Slack (se tiver configurado corretamente)

### Se houver erro (🔴 Red):

1. Clique no step que falhou (ex: "Run Conexa Monitor")
2. Veja a mensagem de erro
3. Erros comuns:
   - API key inválida → verifica secrets
   - Slack webhook inválido → verifica secrets
   - Dependências não instaladas → check requirements.txt

---

## Passo 6: Confirmar Funcionamento

Se você vir isso na console:

```
[OK] SERP buscas: 70
  - Com anúncios: X
  - Sem anúncios: X
[OK] Domínios únicos: X
[OK] Novos domínios detectados: X
[OK] Monitoramento concluído!
```

**PARABÉNS!** Seu workflow está 100% funcionando! 🎉

---

## Próximos Passos

### Automação (sem fazer nada):

- **Segunda-feira 14:00 UTC**: ✓ Executa automaticamente
- **Quarta-feira 14:00 UTC**: ✓ Executa automaticamente  
- **Sexta-feira 14:00 UTC**: ✓ Executa automaticamente

### Você pode:

1. Testar novamente quando quiser (Run workflow manual)
2. Ver histórico de todas as execuções
3. Receber alertas no Slack automáticos
4. Ver artifacts (screenshots, database backup)

---

## URLs Úteis

- **Workflow page**: https://github.com/jarbas-pixiolini/robo_sbn/actions/workflows/competitor-monitor.yml
- **Secrets page**: https://github.com/jarbas-pixiolini/robo_sbn/settings/secrets/actions
- **Repo page**: https://github.com/jarbas-pixiolini/robo_sbn

---

## Checklist

- [ ] Adicionou SERPAPI_API_KEY (Passo 1.2)
- [ ] Adicionou SLACK_WEBHOOK_URL (Passo 1.3)
- [ ] Viu 2 secrets na página Secrets
- [ ] Abriu Actions
- [ ] Clicou "Run workflow"
- [ ] Viu workflow começar (🟡 Yellow)
- [ ] Esperou 2-3 minutos
- [ ] Viu sucesso (🟢 Green)
- [ ] Viu os logs OK
- [ ] Recebeu alerta no Slack

✓ **PRONTO!** Sistema em automação 24/7 🚀

