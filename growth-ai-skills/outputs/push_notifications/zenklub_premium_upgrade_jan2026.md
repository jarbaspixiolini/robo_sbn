# Exemplo: Campanha Push Notification - Zenklub Upgrade

## 📋 Brief Executivo

**Objetivo:** Aumentar assinantes premium do Zenklub entre usuários ativos  
**Segmento:** Usuários free/básico com 2+ sessões nos últimos 30 dias  
**Período:** 3 semanas (Jan 15 - Feb 5, 2026)  
**KPI:** 5% conversion para premium  

---

## 🎯 **Etapa 1: INTAKE (Brief Estruturado)**

```
CANAL: Push Notification (App)
OBJETIVO: Ativação (upgrade para premium)
PÚBLICO: Usuários ativos free (comportamento de engajamento alto)
OFERTA PRINCIPAL: "Acesso ilimitado a psicólogos + 40% OFF no primeiro mês"
CTA PRIMÁRIO: "Ativar Premium Agora"
RESTRIÇÕES:
  - Máximo 2 linhas de título
  - Máximo 4 linhas descrição (120 chars)
  - Sem termos que pareçam "diagnóstico"
  - Compliance check: APROVADO
DURAÇÃO: 21 dias (com STO)
FREQUENCY CAP: Máximo 2 pushes por usuário em 7 dias
```

---

## 🎨 **Etapa 2: CRIAÇÃO (Draft 1 Completo)**

### **Versão Principal: Icon Push**

```
TIPO: Icon Push (sem imagem)

TÍTULO:
"Premium Zenklub: Acesso ilimitado com 40% OFF 🎁"

DESCRIÇÃO:
"Você merece acompanhamento contínuo. Sessões com qualquer psicólogo + chat 24/7."

PERSONALIZAÇÃO:
Título: "Oi {{first_name}}, seu upgrade em 40% OFF 🎁"
Fallback: "Premium Zenklub: Seu upgrade em 40% OFF 🎁"

DEEP LINK:
app://zenklub/premium?campaign_id=promo_jan2026&user_id={{user_id}}&source=push

BOTÕES DE AÇÃO (2):
├─ "Ativar Premium" 
│  └─ app://checkout/premium_plan?campaign_id=promo_jan&user_id={{user_id}}
└─ "Saber Mais"
   └─ https://zenklub.com/premium?utm_source=push&utm_campaign=jan_2026

EMOJIS:
✓ 🎁 (oferta visual)
✓ 💬 (chat, suporte)
✓ Evitar: 🚀 (muito genérico), ⭐ (óbvio)
```

---

## ✅ **Etapa 3: REVISÃO (QA + Compliance)**

### **Checklist de Validação**

| Item | Status | Ajuste |
|------|--------|--------|
| Clareza para leigo | ✓ | "Acesso ilimitado a psicólogos" é óbvio |
| Tom Conexa | ✓ | Próxima ("você merece"), informativa |
| Sem diagnóstico | ✓ | Apenas benefícios, não cura |
| Sem promessa | ✓ | "Acompanhamento" ≠ "cura garantida" |
| CTA claro | ✓ | "Ativar Premium" é específico |
| Personalização funciona | ✓ | {{first_name}} + fallback OK |
| Emojis apropriados | ✓ | 1 emoji, não excessivo |
| Tamanho caracteres | ✓ | Título 57 chars, Desc 118 chars |

### **Versão Final (Post-QA)**

```
TÍTULO (FINAL):
"Oi {{first_name}}, upgrade para Premium com 40% OFF 🎁"
Fallback: "Premium Zenklub: 40% OFF só hoje 🎁"

DESCRIÇÃO (FINAL):
"Sessões com qualquer psicólogo + chat 24/7. Seu bem-estar em primeiro lugar."

BOTÕES (VALIDADOS):
1. "Ativar Premium" (14 chars) ✓
2. "Saber Mais" (10 chars) ✓

PERSONALIZAÇÃO (VALIDADA):
✓ {{first_name}} com fallback "Cliente"
✓ {{user_id}} para rastreamento
✓ {{campaign_id}} para análise
```

---

## 🚀 **Etapa 4: VARIAÇÕES (A/B Testing)**

### **Variante A — Foco em Benefício (60% tráfego)**
```
TIPO: Icon Push
TÍTULO: "Oi {{first_name}}, upgrade para Premium com 40% OFF 🎁"
DESCRIÇÃO: "Sessões com qualquer psicólogo + chat 24/7."
ÂNGULO: Conveniência + comunidade
```

### **Variante B — Foco em Urgência (20% tráfego)**
```
TIPO: Icon Push
TÍTULO: "Oferta expira hoje: Premium com 40% OFF por mais 3h ⏰"
DESCRIÇÃO: "Acesso ilimitado a especialistas. Aproveita agora?"
ÂNGULO: Escassez + urgência temporal
```

### **Variante C — Single Image Push (20% tráfego)**
```
TIPO: Single Image Push
IMAGEM: zenklub_premium_upgrade.png (1024x512, 2:1 aspect)
TÍTULO: "Seu bem-estar em primeiro lugar 💚"
DESCRIÇÃO: "Premium agora com 40% OFF. Sessões ilimitadas."
BOTÕES:
├─ "Ativar" (6 chars)
└─ "Depois" (6 chars)
ÂNGULO: Visual + emocional
```

---

## 📊 **Configuração de Lançamento**

```
SEGMENTAÇÃO:
├─ Usuários com status = "free" ou "basic"
├─ 2+ sessões nos últimos 30 dias
├─ Opt-in push = SIM
└─ Não receberam essa push nos últimos 7 dias

TIMING:
├─ Send Time Optimization: ATIVO
├─ Horário preferido: 10h-14h (baseado em histórico)
├─ TTL (Time To Live): 24 horas
└─ Período de envio: 21 dias (Jan 15 - Feb 5)

FREQUÊNCIA:
├─ Frequency Cap: Máx. 2 pushes por usuário em 7 dias
├─ Message Throttling: Distribuir em 15 minutos (evita pico)
└─ Intervalo mínimo: 48h entre pushes do mesmo usuário

CONFIGURAÇÕES:
├─ Notification Sound: Padrão (não invasivo)
├─ iOS Thread: "premium_offers"
├─ Android Channel: "promotional"
└─ Campaign Tags: ["premium", "upgrade", "january_2026"]
```

---

## 🎯 **Goals & Conversão**

```
GOAL PRIMÁRIO: Click em "Ativar Premium"
├─ Tipo: Button click
├─ Duração: 7 dias (conversão típica)
└─ Sucesso: Completar checkout

GOAL SECUNDÁRIO: Saber Mais
├─ Tipo: Button click
├─ Duração: 3 dias
└─ Ação: Landing page do premium (retargetable)

GOAL TERCIÁRIO: Nenhum click
├─ Tipo: Unsubscribe
├─ Alertar se: > 0.5% desub rate
└─ Ação: Reduzir frequência ou revisar mensagem

ATRIBUIÇÃO:
├─ user_id = rastreamento individual
├─ campaign_id = análise de campanha
└─ utm_source=push&utm_campaign=jan2026 (Google Analytics)
```

---

## 📈 **Análise Esperada**

### **Métricas de Sucesso**

| Métrica | Target | Excelente | Ação se falhar |
|---------|--------|-----------|-----------------|
| Delivery Rate | 88% | 95%+ | Revisar segmentação |
| CTR | 5% | 8%+ | Testar novo assunto |
| Conv. Rate | 2% | 3%+ | Revisar landing page |
| Unsubscribe | <0.3% | <0.2% | Reduzir frequência |
| Revenue | R$ 5k | R$ 10k+ | Ampliar audiência |

### **Painel de Monitoramento (Daily)**
```
DIA 1-3: Entregar 30% da audiência, validar click rate
DIA 4-7: Análise de variante vencedora, pausar variant C se low performance
DIA 8-14: Escalar vencedora, considerar retargeting
DIA 15-21: Relatório final, aprendizados para próxima campanha
```

---

## 💬 **Deep Link & Rastreamento**

```
URL FINAL PARA CHECKOUT:
https://zenklub.com/checkout/premium?
  utm_source=push
  utm_medium=notification
  utm_campaign=jan_2026_premium
  utm_content=variant_a
  user_id=USER123
  campaign_id=promo_jan2026
  ts=TIMESTAMP

DEEP LINK (App):
app://zenklub/checkout/premium?campaign_id=promo_jan2026&variant=a&user_id={{user_id}}

RASTREAMENTO:
├─ GA4: utm_* parameters
├─ Insider One: user_id + campaign_id
├─ Internal DB: Correlacionar com conversão
└─ ROI: Revenue gerado / Custo de envio
```

---

## 🔍 **Checklist Final (Antes de Enviar)**

- [ ] Segmento definido e validado (N > 50k usuários)
- [ ] Todas as 3 variantes testadas em device real
- [ ] Deep links verificados e funcionam
- [ ] Emojis aparecem corretos (iOS + Android)
- [ ] Botões têm tamanho correto (1-3 chars em 3 botões)
- [ ] Fallbacks para personalização testados
- [ ] TTL definido (24h recomendado)
- [ ] Frequency cap ativo (máx 2 em 7 dias)
- [ ] Goals configurados no Insider
- [ ] Tags adicionadas (para análise)
- [ ] Supervisão marcada (alerta se unsubscribe > 0.5%)
- [ ] Relatório pós-envio agendado (7 dias)

---

## 📝 **Saída para Stakeholder**

```
CAMPANHA: Zenklub Premium Upgrade — Jan 2026
PERÍODO: 21 dias (Jan 15 - Feb 5)
AUDIÊNCIA: 120k usuários free/basic ativos
VARIANTES: 3 (Benefício 60% | Urgência 20% | Visual 20%)

EXPECTED RESULTS:
├─ Delivery: ~106k pushes
├─ Clicks: ~5.3k (5% CTR)
├─ Conversões: ~2.1k (2% conv)
├─ Revenue: ~R$ 63k (30 x 2.1k)
└─ ROI: 8-10x (típico para push)

PRÓXIMAS AÇÕES:
1. ✓ Aprovação final (você está aqui)
2. Enviar para QA de compliance (médico)
3. Agendar lançamento
4. Monitorar em tempo real
5. Relatório pós-campanha
```

---

**Pronto para enviar? ✅** Ou precisa fazer ajustes?

