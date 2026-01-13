# Guia de Instalação - Ollama para Windows

## O que é Ollama?

Ollama é uma plataforma que permite executar modelos de linguagem grandes (LLMs) localmente no seu computador, sem dependência de APIs na nuvem.

---

## 📥 Passo 1: Download

1. Acesse: **https://ollama.ai**
2. Clique em **"Download"**
3. Selecione **"Windows"**
4. Faça o download do instalador `.exe`

---

## 💾 Passo 2: Instalação

1. Abra o arquivo baixado (`OllamaSetup.exe`)
2. Siga o assistente de instalação
3. Escolha a pasta de destino (padrão: `C:\Users\[seu_usuario]\AppData\Local\Programs\Ollama`)
4. Clique em **"Install"**
5. Aguarde a conclusão

---

## ✅ Passo 3: Verificar Instalação

Abra o **PowerShell** e execute:

```powershell
ollama --version
```

Se retornar a versão, está instalado corretamente.

---

## 🚀 Passo 4: Baixar um Modelo

No PowerShell, execute:

```powershell
ollama pull llama2
```

Ou outro modelo:
```powershell
ollama pull mistral
ollama pull neural-chat
ollama pull dolphin-mixtral
```

⏳ **Nota:** O download pode levar alguns minutos dependendo do tamanho do modelo.

---

## 🎯 Passo 5: Executar o Modelo

```powershell
ollama run llama2
```

Agora você pode digitar perguntas e receber respostas locais!

---

## 🔗 Passo 6: Integração com Continue.dev (Opcional)

Para usar Ollama com Continue no VS Code:

1. Abra **Continue** (`Ctrl+L`)
2. Vá para **Settings** (engrenagem)
3. Configure o modelo local:

```yaml
models:
  - name: "Ollama Local"
    provider: "ollama"
    model: "llama2"
    apiBase: "http://localhost:11434"
```

---

## 📋 Modelos Disponíveis

| Modelo | Tamanho | Velocidade | Qualidade |
|--------|---------|-----------|-----------|
| **llama2** | 3.5 GB | Rápido | Boa |
| **mistral** | 5 GB | Muito Rápido | Ótima |
| **neural-chat** | 5 GB | Rápido | Excelente |
| **dolphin-mixtral** | 26 GB | Moderado | Excelente |
| **codellama** | 3.5 GB | Rápido | Ótima (código) |

---

## 🛠️ Troubleshooting

### "Comando ollama não encontrado"
- Reinicie o PowerShell após instalar
- Verifique se Ollama foi instalado corretamente
- Tente usar o caminho completo: `C:\Users\[seu_usuario]\AppData\Local\Programs\Ollama\ollama.exe`

### "Modelo não baixa"
- Verifique sua conexão de internet
- Tente com um modelo menor primeiro (llama2)

### "Porta 11434 já em uso"
- Outra instância do Ollama está rodando
- Feche outras janelas de PowerShell com Ollama
- Reinicie seu computador

---

## 🎓 Próximos Passos

1. Experimente rodar o modelo: `ollama run llama2`
2. Integre com Continue.dev para usar IA no editor
3. Explore outros modelos conforme necessário

---

**Ollama instalado e pronto para uso! 🚀**
