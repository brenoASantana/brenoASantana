# 🔄 Sincronização LinkedIn → README

Este repositório está configurado para manter o README automaticamente sincronizado com seu perfil do LinkedIn.

## 📋 Como Funciona

### ✨ Características

- **Atualização Automática Diária**: O README é atualizado automaticamente às 8:00 AM UTC
- **Histórico Limpo**: Sem informações desatualizáveis como datas de empregos
- **Sempre Atemporal**: Apenas informações que não mudam com o tempo
- **Sincronizado com LinkedIn**: Toda mudança no seu perfil pode ser refletida aqui

### 📊 O que NÃO está mais no README

Removidas seções que ficam desatualizadas rapidamente:
- ❌ Experiência Profissional (datas mudam)
- ❌ Voluntariado (projetos mudam)
- ❌ Formação (pode ficar desatualizada)

### ✅ O que Permanece Atemporal

- ✨ Sobre você (genérico e sempre relevante)
- 🛠️ Habilidades Técnicas (linguagens e ferramentas)
- 🎯 Interesses & Paixões
- 📊 Estatísticas do GitHub (atualizadas dinamicamente)

---

## 🔧 Configuração

### Pré-requisitos

- Node.js 18+
- Python 3.11+
- Git

### Instalação

1. **Instale as dependências do script Python**:
```bash
pip install requests beautifulsoup4
```

2. **Configure o GitHub Action** (já incluído em `.github/workflows/sync-linkedin.yml`)

### ⚙️ Variáveis de Ambiente

O workflow já está configurado com:
- `LINKEDIN_PROFILE_ID`: `brenoasantana` (seu username do LinkedIn)
- `GITHUB_TOKEN`: Incluído automaticamente pelo GitHub Actions

---

## 🚀 Uso Manual

Para executar a sincronização manualmente:

```bash
python scripts/sync_linkedin.py
```

Ou via GitHub Actions (na aba "Actions" → "Sincronizar LinkedIn com README" → "Run workflow")

---

## 📈 Próximas Melhorias Possíveis

Você pode expandir este workflow para:

1. **Buscar dados reais do LinkedIn** (com API oficial ou RapidAPI)
   ```python
   # Exemplo com RapidAPI
   import requests

   url = "https://linkedin-data2.p.rapidapi.com/get-profile-with-skills"
   headers = {
       "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
       "X-RapidAPI-Host": "linkedin-data2.p.rapidapi.com"
   }
   response = requests.get(url, headers=headers)
   ```

2. **Atualizar badges com habilidades do LinkedIn**
3. **Sincronizar recomendações**
4. **Atualizar "últimas certificações"**

---

## 📝 Notas

- O script roda todos os dias às 8:00 AM UTC
- Você pode disparar manualmente via GitHub Actions
- Commits são criados automaticamente quando há mudanças
- Histórico completo disponível no Git

---

## 🔗 Links Úteis

- 📌 [Seu Perfil LinkedIn](https://www.linkedin.com/in/brenoasantana/)
- 📊 [GitHub Stats](https://github-readme-stats.vercel.app/)
- 🐍 [Snake Contribution Chart](https://github.com/marketplace/actions/generate-snake)

---

**Última atualização**: Automaticamente gerenciada
