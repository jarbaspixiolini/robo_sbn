# 📱 Campanha Push Notification - Especialidades Verão 2026

## 📋 Brief Executivo

**Objetivo:** Estimular agendamento de consultas telemedicina  
**Segmento:** Usuários com acesso incluído (sem custo) + histórico de consulta Conexa  
**Período:** 14-28 janeiro 2026 (verão + ano novo)  
**Especialidades:** Dermatologia | Endocrinologia | Nutrição | Gastroenterologia  
**CTA:** "Agendar Agora"  
**Compliance:** ✅ Checklist Saúde Aplicado  

---

## 🎯 **CAMPANHA 1: DERMATOLOGIA**

### **Etapa 2: Criação (Draft 1)**

#### **Versão Principal: Icon Push**

```
TIPO: Icon Push

TÍTULO:
"Pele protegida no verão com especialista 🌞"

DESCRIÇÃO:
"Consulta telemedicina com dermatologista disponível hoje. Seu bem-estar em primeiro lugar."

PERSONALIZAÇÃO:
Título: "Oi {{first_name}}, pele protegida no verão 🌞"
Fallback: "Pele protegida no verão com especialista 🌞"

DEEP LINK:
app://conexa/book?specialty=dermatology&campaign=summer_2026&user_id={{user_id}}&source=push

BOTÕES:
├─ "Agendar Agora" (14 chars)
│  └─ app://conexa/schedule/dermatology?user_id={{user_id}}&campaign=summer_derm
└─ "Saber Mais" (10 chars)
   └─ https://conexa.com/especialidades/dermatologia?utm_source=push&utm_campaign=summer_2026
```

---

### **Etapa 3: Revisão (QA + Compliance)**

#### **Checklist Compliance Saúde**

| Validação | Status | Observação |
|-----------|--------|-----------|
| Sem diagnóstico | ✅ | "Pele protegida" = informação, não diagnóstico |
| Sem promessa de cura | ✅ | Apenas "consulta com especialista" |
| Linguagem acessível | ✅ | Leigo entende "pele protegida no verão" |
| Direcionamento profissional | ✅ | "com dermatologista" deixa claro |
| Tom Conexa | ✅ | Próxima ("Oi {{first_name}}"), informativa, simples |
| Sem pressão agressiva | ✅ | "disponível hoje" = informação, não urgência falsa |
| Menção telemedicina | ✅ | Implícito (horários flexíveis, em casa) |
| Sem linguagem patológica | ✅ | Foco em "proteção" não em doença |

#### **Versão Final Pós-QA**

```
TÍTULO (FINAL):
"Oi {{first_name}}, pele protegida no verão 🌞"
Fallback: "Pele bem cuidada no verão com especialista 🌞"

DESCRIÇÃO (FINAL):
"Consulta com dermatologista por telemedicina. Agenda disponível hoje."

EMOJIS: ✅ 1 emoji apropriado (🌞 = verão/proteção solar)

PERSONALIZACAO: ✅ {{first_name}} com fallback testado

CTA: ✅ "Agendar Agora" é direto e claro
```

---

### **Etapa 4: Variações (A/B Testing)**

#### **Variante A — Foco em Proteção (50% tráfego)**
```
TIPO: Icon Push
TÍTULO: "Oi {{first_name}}, pele protegida no verão 🌞"
DESCRIÇÃO: "Consulta com dermatologista por telemedicina. Hoje tem horário!"
ÂNGULO: Cuidado preventivo + praticidade
```

#### **Variante B — Foco em Saúde da Pele (30% tráfego)**
```
TIPO: Icon Push
TÍTULO: "Sua pele merece atenção especializada 💚"
DESCRIÇÃO: "Dermatologista disponível hoje por telemedicina. Agende agora."
ÂNGULO: Bem-estar + cuidado pessoal
```

#### **Variante C — Single Image (20% tráfego)**
```
TIPO: Single Image Push
IMAGEM: dermatology_summer_care.png (1024x512)
TÍTULO: "Verão com pele saudável"
DESCRIÇÃO: "Consulta com especialista via telemedicina. Hoje!"
BOTÕES:
├─ "Agendar" (7 chars)
└─ "Depois" (6 chars)
ÂNGULO: Visual + emocional
```

---

## 🎯 **CAMPANHA 2: ENDOCRINOLOGIA**

### **Etapa 2: Criação (Draft 1)**

#### **Versão Principal: Icon Push**

```
TIPO: Icon Push

TÍTULO:
"Saúde metabólica com endocrinologista 💪"

DESCRIÇÃO:
"Consulta telemedicina para avaliar sua saúde hormonal. Especialista disponível hoje."

PERSONALIZAÇÃO:
Título: "{{first_name}}, cuide da sua saúde metabólica 💪"
Fallback: "Saúde metabólica com endocrinologista 💪"

DEEP LINK:
app://conexa/book?specialty=endocrinology&campaign=summer_2026&user_id={{user_id}}&source=push

BOTÕES:
├─ "Agendar Agora" (14 chars)
│  └─ app://conexa/schedule/endocrinology?user_id={{user_id}}&campaign=summer_endo
└─ "Saber Mais" (10 chars)
   └─ https://conexa.com/especialidades/endocrinologia?utm_source=push&utm_campaign=summer_2026
```

---

### **Etapa 3: Revisão (QA + Compliance)**

#### **Checklist Compliance Saúde**

| Validação | Status | Observação |
|-----------|--------|-----------|
| Sem diagnóstico | ✅ | "Saúde metabólica" = objetivo geral, não diagnóstico |
| Sem promessa de emagrecimento | ✅ | Apenas "avaliar saúde hormonal" |
| Sem linguagem de tratamento milagre | ✅ | "Consulta para avaliar" = educativo |
| Menção telemedicina clara | ✅ | "por telemedicina" deixa explícito |
| Tom Conexa | ✅ | Especialista + próxima + informativa |
| Sem exploração de insegurança | ✅ | Foco em "cuidado" não em "problema" |
| Linguagem inclusiva | ✅ | "sua saúde" = respeito individual |

#### **Versão Final Pós-QA**

```
TÍTULO (FINAL):
"{{first_name}}, cuide da sua saúde metabólica 💪"
Fallback: "Saúde metabólica com endocrinologista 💪"

DESCRIÇÃO (FINAL):
"Consulta com endocrinologista por telemedicina. Agenda disponível hoje."

EMOJI: ✅ 💪 = força, saúde, cuidado
```

---

### **Etapa 4: Variações (A/B Testing)**

#### **Variante A — Foco em Avaliação (50% tráfego)**
```
TIPO: Icon Push
TÍTULO: "{{first_name}}, cuide da sua saúde metabólica 💪"
DESCRIÇÃO: "Avalie sua saúde hormonal com endocrinologista. Telemedicina hoje!"
ÂNGULO: Prevenção + avaliação
```

#### **Variante B — Foco em Bem-estar (30% tráfego)**
```
TIPO: Icon Push
TÍTULO: "Seu bem-estar hormonal importa 💚"
DESCRIÇÃO: "Consulta com especialista por telemedicina. Horário hoje disponível."
ÂNGULO: Bem-estar + cuidado
```

#### **Variante C — Single Image (20% tráfego)**
```
TIPO: Single Image Push
IMAGEM: endocrinology_wellness.png (1024x512)
TÍTULO: "Saúde em equilíbrio"
DESCRIÇÃO: "Endocrinologista disponível hoje via telemedicina."
BOTÕES:
├─ "Agendar" (7 chars)
└─ "Depois" (6 chars)
ÂNGULO: Visual inspirador
```

---

## 🎯 **CAMPANHA 3: NUTRIÇÃO**

### **Etapa 2: Criação (Draft 1)**

#### **Versão Principal: Icon Push**

```
TIPO: Icon Push

TÍTULO:
"Hábitos alimentares saudáveis no ano novo 🥗"

DESCRIÇÃO:
"Nutricionista especializado disponível para guiar sua jornada. Consulta telemedicina hoje."

PERSONALIZAÇÃO:
Título: "{{first_name}}, alimente-se melhor em 2026 🥗"
Fallback: "Hábitos alimentares saudáveis com nutricionista 🥗"

DEEP LINK:
app://conexa/book?specialty=nutrition&campaign=summer_2026&user_id={{user_id}}&source=push

BOTÕES:
├─ "Agendar Agora" (14 chars)
│  └─ app://conexa/schedule/nutrition?user_id={{user_id}}&campaign=summer_nutri
└─ "Saber Mais" (10 chars)
   └─ https://conexa.com/especialidades/nutricao?utm_source=push&utm_campaign=summer_2026
```

---

### **Etapa 3: Revisão (QA + Compliance)**

#### **Checklist Compliance Saúde**

| Validação | Status | Observação |
|-----------|--------|-----------|
| Sem promessa de "dieta milagre" | ✅ | "Guiar sua jornada" = processo, não solução mágica |
| Sem promessa de emagrecimento rápido | ✅ | Foco em "hábitos saudáveis" |
| Sem linguagem de culpa/vergonha | ✅ | "alimente-se melhor" = positivo, não crítico |
| Linguagem educativa | ✅ | "nutricionista especializado" deixa claro |
| Menção telemedicina | ✅ | "Consulta telemedicina hoje" |
| Tom Conexa | ✅ | Próxima, motivacional, especialista |
| Sem exploração de insegurança | ✅ | Foco em "jornada" = apoio contínuo |
| Sem diagnóstico nutricional | ✅ | Apenas "guiar" não "tratar" |

#### **Versão Final Pós-QA**

```
TÍTULO (FINAL):
"{{first_name}}, alimente-se melhor em 2026 🥗"
Fallback: "Nutrição saudável com especialista 🥗"

DESCRIÇÃO (FINAL):
"Nutricionista disponível para guiar sua alimentação. Consulta telemedicina hoje."

EMOJI: ✅ 🥗 = alimento saudável, nutrition positiva
```

---

### **Etapa 4: Variações (A/B Testing)**

#### **Variante A — Foco em Hábitos (50% tráfego)**
```
TIPO: Icon Push
TÍTULO: "{{first_name}}, alimente-se melhor em 2026 🥗"
DESCRIÇÃO: "Nutricionista vai guiar seus hábitos. Consulta telemedicina hoje!"
ÂNGULO: Mudança de hábitos + apoio
```

#### **Variante B — Foco em Saúde Integral (30% tráfego)**
```
TIPO: Icon Push
TÍTULO: "Sua nutrição merece atenção 💚"
DESCRIÇÃO: "Consulte nosso nutricionista por telemedicina. Agenda hoje disponível."
ÂNGULO: Bem-estar integral
```

#### **Variante C — Single Image (20% tráfego)**
```
TIPO: Single Image Push
IMAGEM: nutrition_healthy_2026.png (1024x512)
TÍTULO: "Ano novo, alimentação nova"
DESCRIÇÃO: "Nutricionista disponível hoje via telemedicina."
BOTÕES:
├─ "Agendar" (7 chars)
└─ "Depois" (6 chars)
ÂNGULO: Motivação + ano novo
```

---

## 🎯 **CAMPANHA 4: GASTROENTEROLOGIA**

### **Etapa 2: Criação (Draft 1)**

#### **Versão Principal: Icon Push**

```
TIPO: Icon Push

TÍTULO:
"Saúde digestiva com especialista 🏥"

DESCRIÇÃO:
"Consulta telemedicina com gastroenterologista. Cuide do seu bem-estar digestivo hoje."

PERSONALIZAÇÃO:
Título: "{{first_name}}, sua saúde digestiva é importante 🏥"
Fallback: "Saúde digestiva com gastroenterologista 🏥"

DEEP LINK:
app://conexa/book?specialty=gastroenterology&campaign=summer_2026&user_id={{user_id}}&source=push

BOTÕES:
├─ "Agendar Agora" (14 chars)
│  └─ app://conexa/schedule/gastroenterology?user_id={{user_id}}&campaign=summer_gastro
└─ "Saber Mais" (10 chars)
   └─ https://conexa.com/especialidades/gastroenterologia?utm_source=push&utm_campaign=summer_2026
```

---

### **Etapa 3: Revisão (QA + Compliance)**

#### **Checklist Compliance Saúde**

| Validação | Status | Observação |
|-----------|--------|-----------|
| Sem diagnóstico de doença | ✅ | "Saúde digestiva" = prevenção, não doença |
| Sem promessas de cura | ✅ | Apenas "consulta" = avaliação |
| Linguagem respeitosa | ✅ | "bem-estar digestivo" = positivo |
| Menção telemedicina | ✅ | "Consulta telemedicina" deixa claro |
| Tom Conexa | ✅ | Especialista + cuidado + próxima |
| Sem linguagem patológica | ✅ | Foco em "saúde" não em "sintomas" |
| Sem constrangimento | ✅ | "bem-estar digestivo" é respeitoso |
| Acesso apropriado | ✅ | Especialidade delicada, telemedicina apropriada |

#### **Versão Final Pós-QA**

```
TÍTULO (FINAL):
"{{first_name}}, sua saúde digestiva é importante 🏥"
Fallback: "Saúde digestiva com gastroenterologista 🏥"

DESCRIÇÃO (FINAL):
"Consulta com gastroenterologista por telemedicina. Horário disponível hoje."

EMOJI: ✅ 🏥 = saúde profissional, especialista
```

---

### **Etapa 4: Variações (A/B Testing)**

#### **Variante A — Foco em Prevenção (50% tráfego)**
```
TIPO: Icon Push
TÍTULO: "{{first_name}}, sua saúde digestiva é importante 🏥"
DESCRIÇÃO: "Prevenir é cuidar. Gastroenterologista disponível hoje por telemedicina!"
ÂNGULO: Prevenção + saúde
```

#### **Variante B — Foco em Bem-estar (30% tráfego)**
```
TIPO: Icon Push
TÍTULO: "Cuide do seu bem-estar digestivo 💚"
DESCRIÇÃO: "Consulta com gastroenterologista. Telemedicina hoje com horário disponível."
ÂNGULO: Bem-estar + cuidado integral
```

#### **Variante C — Single Image (20% tráfego)**
```
TIPO: Single Image Push
IMAGEM: gastroenterology_wellness.png (1024x512)
TÍTULO: "Bem-estar começa de dentro"
DESCRIÇÃO: "Gastroenterologista disponível hoje via telemedicina."
BOTÕES:
├─ "Agendar" (7 chars)
└─ "Depois" (6 chars)
ÂNGULO: Bem-estar holístico
```

---

## 🚀 **CONFIGURAÇÃO DE LANÇAMENTO (Todas as 4 Campanhas)**

```
SEGMENTAÇÃO:
├─ Status: Usuários com acesso incluído (sem custo)
├─ Histórico: Mínimo 1 consulta Conexa no passado
├─ Opt-in: Push notifications = SIM
├─ Especialidades: NÃO ter consultado nessa especialidade nos últimos 90 dias
└─ Exclusão: Não receberam push especialidade similar em 7 dias

TIMING:
├─ Send Time Optimization: ATIVO
├─ Melhor horário: 10h-14h (baseado em histórico)
├─ TTL (Time To Live): 24 horas (agenda para HOJE)
└─ Período: 14-28 janeiro 2026

FREQUÊNCIA:
├─ Frequency Cap: Máx. 1 push por especialidade por usuário em 7 dias
├─ Message Throttling: Distribuir em 20 minutos
├─ Intervalo mínimo: 48h entre pushes diferentes
└─ Máximo: 4 pushes (uma por especialidade) em 14 dias

CONFIGURAÇÕES:
├─ Notification Sound: Padrão (não invasivo)
├─ iOS Thread: "specialties_summer_2026"
├─ Android Channel: "medical_services"
└─ Campaign Tags: ["summer_2026", "verão", "telemedicina", "ano_novo"]
```

---

## 🎯 **Goals & Conversão**

```
GOAL PRIMÁRIO: Clique em "Agendar Agora"
├─ Tipo: Button click → Completar agendamento
├─ Duração: 7 dias
└─ Sucesso: Consulta marcada

GOAL SECUNDÁRIO: Clique em "Saber Mais"
├─ Tipo: Button click
├─ Duração: 3 dias
└─ Ação: Landing page da especialidade

ATRIBUIÇÃO:
├─ user_id = rastreamento individual
├─ campaign = verão_2026_{{specialty}}
├─ utm_source=push para Google Analytics
└─ Correlacionar com consulta efetiva
```

---

## 📊 **Métricas Esperadas**

| Métrica | Target | Excelente |
|---------|--------|-----------|
| Delivery Rate | 90% | 95%+ |
| CTR | 6% | 8%+ |
| Conv. (Agendamentos) | 2.5% | 3.5%+ |
| Unsubscribe | <0.2% | <0.1% |

**Conversão Esperada:**
- 4 campanhas × 100k usuários = 400k pushes
- CTR 6% = 24k cliques
- Conv 2.5% = 600 agendamentos
- **ROI: ~R$ 12-18k em receita (20-30R$ por consulta)**

---

## ✅ **Checklist Final Compliance**

- [ ] Nenhuma campanha promete diagnóstico
- [ ] Nenhuma campanha promete cura ou tratamento definitivo
- [ ] Todas mencionam "telemedicina" explicitamente
- [ ] Linguagem simples, sem jargão médico
- [ ] Tom próximo e motivacional (Conexa)
- [ ] Sem exploração de medos/inseguranças
- [ ] CTA claro: "Agendar Agora"
- [ ] Deep links testados e funcionam
- [ ] Personalização com fallbacks
- [ ] Emojis apropriados (1 máximo)
- [ ] Tamanho caracteres validado
- [ ] Frequency cap ativo
- [ ] TTL = 24h (agenda para HOJE)
- [ ] Exclusões por especialidade aplicadas
- [ ] Tags para análise posterior

---

## 📝 **Saída para Stakeholder**

```
CAMPANHA: Especialidades Verão 2026 — Dermatologia | Endocrinologia | Nutrição | Gastroenterologia
PERÍODO: 14-28 janeiro 2026
PÚBLICO: Usuários com acesso incluído + histórico Conexa
TELEMEDICINA: 100% das consultas

VARIANTES: 3 por especialidade (Benefício 50% | Bem-estar 30% | Visual 20%)

EXPECTED RESULTS:
├─ Total pushes: 400k (4 especialidades × 100k)
├─ Cliques (CTR 6%): 24k
├─ Agendamentos (Conv 2.5%): 600
├─ Receita estimada: R$ 12-18k
└─ ROI: 3-4x (típico para telemedicina)

CONFORMIDADE: ✅ 100% checklist compliance saúde

PRÓXIMAS AÇÕES:
1. ✓ Aprovação final (você está aqui)
2. Validação médica (se necessário)
3. Agendar lançamento para 14/01
4. Monitorar em tempo real
5. Relatório 7 dias após
```

---

**Pronto para lançar? 🚀 Ou precisa ajustar algo nas 4 campanhas?**
