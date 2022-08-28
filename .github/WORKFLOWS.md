# 🤖 GitHub Actions Workflows

Este repositório contém workflows automatizados que mantêm o README sempre atualizado e com a cobrinha devoradora de commits em movimento!

## 📋 Workflows Configurados

### 1. **Generate Snake Animation** 🐍
- **Arquivo:** `.github/workflows/generate-snake.yml`
- **Frequência:** Diariamente (00:00 UTC) + ao fazer push
- **O que faz:** Gera a animação da cobrinha que "devora" seus commits
- **Saída:** Armazena os SVGs no branch `output`

### 2. **Update README with Recent Repos** 📚
- **Arquivo:** `.github/workflows/update-readme.yml`
- **Frequência:** Toda segunda-feira (00:00 UTC) + manual
- **O que faz:** Busca os 3 repositórios mais recentemente atualizados e insere no README
- **Script:** `.github/scripts/update-readme.py`

## 🚀 Como Ativar

Os workflows já estão configurados e rodando automaticamente! Você pode também disparar manualmente:

1. Vá para `Actions` no seu repositório
2. Selecione o workflow desejado
3. Clique em `Run workflow`

## 🔧 Customização

### Alterar frequência de atualização:
Edite os `cron` expressions nos arquivos `.yml`:
- `0 0 * * 1` = Toda segunda-feira à 00:00
- `0 0 * * *` = Todos os dias à 00:00

### Alterar número de repositórios:
Edite em `.github/scripts/update-readme.py`:
```python
'per_page': 3,  # Mude para o número desejado
```

---

**Desenvolvido automaticamente por GitHub Actions! 🤖**
