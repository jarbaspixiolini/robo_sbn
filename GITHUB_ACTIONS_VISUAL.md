# 📋 Teste do GitHub Actions - Passo a Passo Visual

## PASSO 1: Adicionar Secrets (2 min)

```
GitHub.com
  └─ robo_sbn (seu repo)
      └─ Settings (topo direito) 
          └─ Secrets and variables
              └─ Actions
                  └─ [New repository secret] (botão)
```

### Adicione 2 secrets:

**Secret 1:**
```
Name:   SERPAPI_API_KEY
Value:  3f70e47910d8b5833d3c915284949211966fb0a0d97738a1698bce035a671768
Action: [Add secret]
```

**Secret 2:**
```
Name:   SLACK_WEBHOOK_URL
Value:  https://hooks.slack.com/triggers/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
Action: [Add secret]
```

**Resultado esperado:**
```
✓ SERPAPI_API_KEY ••••••••••••••••••
✓ SLACK_WEBHOOK_URL ••••••••••••••••
```

---

## PASSO 2: Ir para Actions (30 seg)

```
GitHub.com/jarbas-pixiolini/robo_sbn
  └─ [Actions] (na barra do topo)
      └─ "Conexa Monitor - Competitor Intelligence" (na esquerda)
```

---

## PASSO 3: Disparar Workflow (1 min)

```
Conexa Monitor - Competitor Intelligence
  └─ [Run workflow] (botão azul na direita)
      └─ branch: main (confirma)
          └─ [Run workflow] (confirma no dropdown)
```

**Resultado esperado:**
```
Seu workflow agora está:
  Status: 🟡 In progress
  Tempo: 0 seg até agora
```

---

## PASSO 4: Acompanhar (2-3 min)

A página atualiza automaticamente. Você verá:

```
monitor (job)
  ✓ Checkout code (10 seg)
  ✓ Set up Python 3.11 (20 seg)
  ✓ Cache pip packages (5 seg)
  ✓ Install dependencies (30 seg)
  🟡 Run Conexa Monitor (45 seg) ← Aguarde aqui
  ⏳ Upload artifacts
  ⏳ Commit database changes
```

---

## PASSO 5: Ver Resultado (quando terminar)

### SUCESSO (🟢 Green):

```
✓ All checks passed

[OK] SERP buscas: 70
  - Com anúncios: 14
  - Sem anúncios: 56
[OK] Domínios únicos: 27
[OK] Novos domínios: X
[OK] Monitoramento concluído!
```

**Você receberá SLACK:**
```
[Slack #channel]
Conexa Monitor - 70 buscas realizadas
Com anúncios: 14
Novos domínios: X
Status: OK
```

### ERRO (🔴 Red):

Se vir vermelho, clique no step que falhou:

**Erro comum 1: Secret inválido**
```
ERROR: 401 Unauthorized
→ Volte ao Step 1, verifique as 2 secrets
```

**Erro comum 2: API key errada**
```
ERROR: 400 Bad Request
→ Copie corretamente a API key do SerpAPI
```

---

## RESUMO VISUAL

```
┌─────────────────────────────────────┐
│  GitHub Actions Workflow Tester     │
├─────────────────────────────────────┤
│                                     │
│  1️⃣  Add Secrets (2 min)             │
│      SERPAPI_API_KEY                │
│      SLACK_WEBHOOK_URL              │
│                                     │
│  2️⃣  Go to Actions (30 sec)          │
│      Conexa Monitor menu            │
│                                     │
│  3️⃣  Run workflow (1 min)            │
│      [Run workflow] button          │
│                                     │
│  4️⃣  Wait (2-3 min)                  │
│      🟡 In progress...              │
│                                     │
│  5️⃣  See results (1 min)             │
│      🟢 Success!                    │
│      or 🔴 Error                    │
│                                     │
│  6️⃣  Check Slack                     │
│      Alerta recebido ✓              │
│                                     │
└─────────────────────────────────────┘
        Tempo total: ~10 min
```

---

## Links Diretos

```
Secrets:  https://github.com/jarbas-pixiolini/robo_sbn/settings/secrets/actions
Actions:  https://github.com/jarbas-pixiolini/robo_sbn/actions
Workflow: https://github.com/jarbas-pixiolini/robo_sbn/actions/workflows/competitor-monitor.yml
```

---

## ✓ Checklist de Teste

```
[ ] 1. Copiei SERPAPI_API_KEY corretamente
[ ] 2. Copiei SLACK_WEBHOOK_URL corretamente  
[ ] 3. Adicionei 2 secrets no GitHub
[ ] 4. Vi 2 secrets criados (✓ checkmark)
[ ] 5. Fui para Actions → Conexa Monitor
[ ] 6. Cliquei [Run workflow]
[ ] 7. Workflow começou (🟡 Yellow)
[ ] 8. Aguardei 2-3 minutos
[ ] 9. Viu resultado (🟢 Green ou 🔴 Red)
[ ] 10. Se Green: Pronto! Se Red: Verifique logs
```

---

**Quando terminar, seu sistema estará:**
✓ Testado  
✓ Validado  
✓ Pronto para automação 3x/semana  
✓ Com alertas Slack em tempo real  

**Tempo total: ~10 minutos** ⏱️

