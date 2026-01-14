# Push Notification - Skill

## 📱 Sobre Push Notifications

Push notifications são mensagens enviadas diretamente para os dispositivos móveis dos usuários. São ideais para:
- **Promoções e ofertas** com urgência
- **Avisos importantes** e atualizações
- **Reengajamento** de usuários inativos
- **Ações diretas** com CTAs interativas

---

## 🎯 **Processo de Criação (7 Passos Insider)**

### **1. CRIAR CAMPANHA**
Acesso: **Experience > Message > App Push > Single Push > Create**

**Tipo de Push:**
- **Icon Push**: Sem imagem, apenas ícone do app + título + descrição
- **Single Image Push**: Com imagem + título + descrição

**Recomendações:**
- ✓ Sempre escolher um tipo baseado no objetivo
- ✓ Icon push é melhor para mensagens simples e rápidas
- ✓ Single image push é melhor para promoções visuais

---

### **2. SELECIONAR SEGMENTO**

**Tipos de Segmentos Disponíveis:**
- Predefined Segments (prontos)
- Standard Segments (padrão)
- Predictive Segments (IA)
- Integrated Segments (dados externos)
- RFM Segments (comportamento)
- Saved Segments (salvos)

**Dicas:**
- ✓ Segmentar por opt-in = usuários que aceitaram receber push
- ✓ Usar segmentos comportamentais para releância
- ✓ Testar com segmentos menores primeiro

---

### **3. DESIGN DA MENSAGEM**

#### **A) Título + Descrição**
```
Título: "Tema principal" (máximo impactante)
Descrição: "Contexto + ação" (máximo 120 caracteres)

Exemplo:
Título: "Você tem uma oferta especial ☀️"
Descrição: "Aproveite 30% OFF em terapia online hoje"
```

#### **B) Personalização com Atributos**
Use **Add Dynamic Content** para personalizar:
```
Título: "Olá {{first_name}}, temos uma oferta!"
Descrição: "Sua próxima sessão {{therapist_name}} com 20% OFF"

⚠️ Sempre incluir fallback:
- first_name → fallback: "Cliente especial"
- therapist_name → fallback: "com nossos especialistas"
```

#### **C) Deep Links (Redirecionamento)**
```
Tipos de Deep Links:
1. Deeplink genérico: app://screen/promo
2. Deeplink com parâmetro: app://product/{{product_id}}
3. URL: https://conexasaude.com/promo

Usar atributos:
- {{user_id}} para rastrear quem clicou
- {{campaign_id}} para análise de performance
```

#### **D) Imagem para Single Image Push**
```
Especificações:
- Formatos: JPG, JPEG, PNG, GIF
- Tamanho máximo: 2 MB
- Dimensões máximas: 2048x2048 px
- Tamanho recomendado: 1024x512 px (2:1 aspect ratio)

Design:
✓ Imagem clara com foco principal no centro
✓ Texto mínimo na imagem (título do app faz isso)
✓ Branding discreto (logo pequeno)
✓ Cores vibrantes mas não agressivas
```

#### **E) Botões de Ação (CTA Buttons)**
**Máximo: 3 botões por push**

```
1 botão → até 48 caracteres
  Ex: "Agendar sessão agora"

2 botões → até 20 caracteres cada
  Ex: "SIM" | "Depois"

3 botões → até 11 caracteres cada
  Ex: "SIM" | "NÃO" | "TAL"
```

**Versão Mínima Necessária:**
- iOS 13.10.0+
- Android 14.9.1+
- Flutter 3.17.0+
- React Native 6.8.0+

**Dicas:**
- ✓ 1 botão = simples, conversão direta
- ✓ 2 botões = decisão sim/não
- ✓ 3 botões = múltiplas opções
- ✓ Usar verbos de ação: "Aproveitar", "Saber Mais", "Agendar"
- ✓ Botões podem ser rastreados para segmentação futura

#### **F) Emojis e IA**
```
Adicionar Emojis:
- 1-2 emojis máximo no título
- Emojis relevantes: 😊 💆‍♀️ 🎁 ⏰ 🔥 ✨
- Evitar: emojis abstratos ou muito diferentes

Gerar com IA:
1. Clique "Generate Text"
2. Insira prompt: "Push sobre promoção de saúde mental"
3. Selecione: Industry (Healthcare) + Use Case (Promotion)
4. Marque "Include Emojis" se quiser
5. Escolha uma das 5 sugestões
6. Clique "Apply"
```

#### **G) Teste de A/B/C**
```
Por padrão: Control Group + Variant A

Aumentar complexidade:
1. Clique "+" ao lado do variant
2. Configure percentual de teste (20% para variant, 80% para controle)
3. Teste até 3 variantes diferentes

Exemplo:
- Controle (60%): "Promoção de terapia"
- Variant A (20%): "Oferta exclusiva para você"
- Variant B (20%): "Tempo limitado: 30% OFF"
```

---

### **4. TESTAR CAMPANHA**

**Antes de enviar:**
1. Clique **"Test Message"**
2. Selecione um **test group** ou **usuário individual**
3. Receba a push no seu dispositivo
4. Valide:
   - ✓ Texto aparece correto
   - ✓ Imagem carrega bem
   - ✓ Botões funcionam
   - ✓ Deep link redireciona corretamente
   - ✓ Emojis aparecem

**Checklist de Teste:**
- [ ] Mensagem é clara e relevante
- [ ] Imagem (se houver) é nítida
- [ ] CTA é visível
- [ ] Deep link funciona
- [ ] Não há erros de personalização
- [ ] Aspecto bom em iOS e Android

---

### **5. SELECIONAR GOALS**

**Objetivos de Conversão:**
```
Tipos de Goals:
1. Clique na notificação
2. Clique em botão específico
3. Ação dentro do app (ex: agendou sessão)
4. Compra/conversão

Duração de Conversão:
- 24h: conversões rápidas (promoções)
- 7 dias: compras típicas
- 30 dias: objetivos de longo prazo
- Customizado: seu próprio período
```

---

### **6. CONFIGURAR LANÇAMENTO**

#### **A) Send Time Optimization (STO)**
```
Enviar no melhor horário para cada usuário:
- Horário usual em que costuma abrir apps
- Histórico de interação
- Fuso horário do usuário

✓ Ativa automaticamente melhor performance
```

#### **B) Time to Live (TTL)**
```
Quanto tempo manter a push na fila se usuário offline:
- 24h: padrão para promoções
- 48h: para avisos importantes
- 7 dias: para conteúdo evergreen
- 0h: urgente, não fila (apenas se online)

Recomendação: 24h para ofertas, 48h para avisos
```

#### **C) Frequency Capping**
```
Limitar quantas pushes um usuário recebe:
- Por dia: máx. 3-5 pushes/dia
- Por semana: máx. 10-15 pushes/semana
- Por mês: máx. 20-30 pushes/mês

Recomendação: 
- Promoções: 1-2 por semana
- Avisos: conforme necessário
- Reengajamento: 2-3 por semana
```

#### **D) Message Throttling**
```
Espaçar envios para não sobrecarregar infraestrutura:
- Enviar em lotes ao longo do tempo
- Exemplo: 50 mil users → distribuir em 10 minutos

✓ Evita picos de carga
✓ Melhora taxas de entrega
```

#### **E) Notification Sounds**
```
iOS: Som padrão do sistema
Android: Som customizado ou padrão

Recomendação:
- Som padrão para maioria (não invasivo)
- Som customizado apenas para alertas urgentes
```

#### **F) iOS Thread & Android Channels**
```
iOS Thread:
- Agrupar múltiplas pushes em "conversa"
- Ex: threadId = "promoções_saude"

Android Channels:
- Categoria do canal
- Ex: channel = "promotions" (permite silenciar por tipo)

Benefício: Usuários controlam notificações por tipo
```

#### **G) Campaign Tags**
```
Adicione tags para organização:
- health_promotion
- engagement_campaign
- seasonal_offer
- test_ab

Facilita: Filtro, análise e reutilização
```

---

### **7. VERIFICAR ANALYTICS**

**Métricas Principais:**
```
1. Delivery Rate
   - % de pushes entregues com sucesso
   - Esperado: 85-95%

2. Click-Through Rate (CTR)
   - % que clicaram na notificação
   - Esperado: 3-8%

3. Conversion Rate
   - % que completaram goal
   - Esperado: 0.5-2%

4. Unsubscribe Rate
   - % que desativaram push
   - Mantém abaixo de 0.5%

5. Bounce Rate
   - Dispositivos offline/inválidos
   - Esperado: 2-5%
```

**Gráficos e Análises:**
- Pie chart: Distribuição de resultados
- Timeline: Performance ao longo do tempo
- Variant comparison: A/B/C results
- Botão clicks: Qual botão converteu melhor

**Export:**
- Exporte dados para relatório
- Formato: CSV/Excel
- Use para dashboards e análises

---

## 💡 **Template de Push Notification**

```
TIPO: Single Image Push

SEGMENTO: Usuários ativos | Opt-in: SIM | Últimos 30 dias

DESIGN:
├─ Título: "Transforme sua saúde mental 🌟"
├─ Descrição: "Sessão com especialista + 30% OFF hoje"
├─ Imagem: therapy_promo_1024x512.png (2:1)
└─ Botões:
   ├─ "Agendar Agora" → app://book_session?campaign_id=X
   └─ "Saber Mais" → https://conexa.com/promo

PERSONALIZAÇÃO:
- Título: "Olá {{first_name}}, transforme sua saúde 🌟"
- Fallback: "Olá, transforme sua saúde 🌟"

DEEP LINK:
- Parâmetros: utm_source=push&utm_campaign=health_promo&user_id={{user_id}}

TESTE:
- Enviar para 10 usuários
- Validar em iOS e Android
- Verificar cliques nos botões

GOALS:
- Meta: Clique em "Agendar Agora"
- Duração: 7 dias

LANÇAMENTO:
- STO: Ativo
- TTL: 24 horas
- Frequency Cap: Máx. 1/semana para este usuário
- Throttling: Distribuir em 5 minutos
- Sound: Padrão
- Tags: health_promo, spring_2026

ANALYTICS:
- Monitorar CTR mínimo de 4%
- Conversion rate mínimo de 1%
- Unsubscribe rate máximo de 0.3%
```

---

## 🎓 **Boas Práticas**

### ✅ **O QUE FAZER**
- ✓ Usar linguagem conversacional e amigável
- ✓ Criar urgência com datas/horários
- ✓ Personalizar com nome/preferências
- ✓ Incluir apenas 1 CTA principal
- ✓ Testar em múltiplos devices
- ✓ Analisar A/B para otimizar
- ✓ Respeitar frequency capping
- ✓ Usar emoji estrategicamente (1-2 max)

### ❌ **O QUE EVITAR**
- ✗ Mensagens genéricas sem personalização
- ✗ Mais de 3 botões ou CTAs
- ✗ Encher de exclamações e emojis
- ✗ Omitir opt-in verification
- ✗ Enviar sem testar antes
- ✗ Ignorar unsubscribe rate
- ✗ Reutilizar mesma mensagem > 2x
- ✗ Não respeitar preferências de horário

---

## 📊 **Métricas de Sucesso**

| Métrica | Baseline | Excelente |
|---------|----------|-----------|
| Delivery Rate | 85-90% | 95%+ |
| CTR | 3-5% | 7-10%+ |
| Conversion | 0.5-1% | 2%+ |
| Unsubscribe | < 1% | < 0.3% |
| A/B Lift | - | +15% |

---

## 🔗 **Recursos**
- [Documentação Insider - Single App Push](https://academy.insiderone.com/docs/single-app-push)
- [Use Cases](https://academy.useinsider.com/docs/use-cases-for-single-app-push)
- [Deep Links Guide](https://academy.useinsider.com/docs/deep-links)
- [Segmentation](https://academy.useinsider.com/docs/single-app-push-segments)

---

**Versão**: 1.0 | **Atualizado**: Janeiro 2026 | **Status**: ✓ Pronto para Uso
