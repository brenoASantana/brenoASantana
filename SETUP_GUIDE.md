# 🔧 Guia de Configuração - LinkedIn Sync

Este guia explica como configurar e estender a sincronização automática entre LinkedIn e README.

---

## 📋 O que foi criado

### 1. **GitHub Action** (`.github/workflows/sync-linkedin.yml`)
- Executa automaticamente todos os dias às 8:00 AM UTC
- Checa se há mudanças no README
- Faz commit automático se houver alterações

### 2. **Script Python** (`scripts/sync_linkedin.py`)
- Gerencia a sincronização de dados
- Atualiza timestamp do README
- Pronto para integração com APIs externas

### 3. **README Simplificado**
- Removidas seções com datas que ficam desatualizadas
- Mantém apenas informações atemporais
- Referência clara ao LinkedIn para detalhes profissionais

---

## 🚀 Como Habilitar Dados Reais do LinkedIn

### Opção 1: RapidAPI (Recomendado)

#### Passo 1: Criar conta na RapidAPI
1. Acesse [rapidapi.com](https://rapidapi.com)
2. Crie uma conta gratuita (você ganha 3 requisições grátis/mês)
3. Procure por "linkedin-data2"

#### Passo 2: Obter API Key
1. Vá para [sua dashboard](https://rapidapi.com/user/dashboard)
2. Copie sua "X-RapidAPI-Key"

#### Passo 3: Adicionar ao GitHub
1. Vá para seu repositório → Settings → Secrets and variables → Actions
2. Clique em "New repository secret"
3. Nome: `RAPIDAPI_KEY`
4. Valor: Cole sua chave da RapidAPI

#### Passo 4: Ativar no script
Descomente esta linha em `scripts/sync_linkedin.py`:
```python
# data.update(self._fetch_from_rapidapi())
```

### Opção 2: LinkedIn Official API

#### Requisitos
- Aproação da LinkedIn (pode levar semanas)
- Application ID e Access Token
- [Documentação Official](https://docs.microsoft.com/en-us/linkedin/)

---

## 📊 Dados que Podem Ser Sincronizados

Com a API configurada, o script pode atualizar:

```python
{
    'headline': str,           # "Full-Stack Developer at Globo"
    'about': str,             # Seção "Sobre" do LinkedIn
    'skills': list,           # Habilidades listadas
    'certifications': list,   # Certificações
    'experience': list,       # Experiências (com datas)
    'education': list,        # Formação
}
```

---

## 🔄 Executar Sincronização Manualmente

### Via CLI (local)
```bash
# Instalar dependências (uma vez)
pip install requests beautifulsoup4

# Executar script
python scripts/sync_linkedin.py
```

### Via GitHub Actions
1. Vá para "Actions" no seu repositório
2. Selecione "Sincronizar LinkedIn com README"
3. Clique "Run workflow"
4. Escolha a branch: `main`

---

## 📝 Estrutura de Pastas

```
brenoASantana/
├── .github/
│   └── workflows/
│       └── sync-linkedin.yml          # ✨ Automation workflow
├── scripts/
│   └── sync_linkedin.py               # 🐍 Script Python
├── README.md                          # 📄 Seu perfil (atualizado)
└── LINKEDIN_SYNC.md                   # 📚 Documentação
```

---

## 🐛 Troubleshooting

### Script falha localmente
```bash
# Verifique se Python 3.11+ está instalado
python --version

# Instale dependências
pip install -r requirements.txt
# (Crie requirements.txt se não existir)
```

### GitHub Action não executa
1. Verifique se workflow está ativado (Settings → Actions)
2. Veja os logs em "Actions" tab
3. Confirme que secrets estão configurados corretamente

### Commits não aparecem
- GitHub Actions usa token padrão
- Se quiser atribuir a seu usuário, crie um PAT (Personal Access Token)
- Adicione como secret: `GITHUB_TOKEN`

---

## 🔗 Próximos Passos (Opcional)

### Nível 1: Avançado Básico
- [ ] Adicionar API key da RapidAPI
- [ ] Habilitar sincronização de habilidades
- [ ] Incluir "últimas certificações"

### Nível 2: Intermediário
- [ ] Criar seção dinâmica de recomendações
- [ ] Sincronizar educação
- [ ] Adicionar validação de dados

### Nível 3: Avançado
- [ ] Usar LinkedIn Official API
- [ ] Integrar com database (PostgreSQL)
- [ ] Criar webhook listener
- [ ] Sincronizar em tempo real

---

## 📚 Recursos Úteis

- 📖 [GitHub Actions Docs](https://docs.github.com/en/actions)
- 🔌 [RapidAPI Docs](https://rapidapi.com/docs)
- 🐍 [Python Requests](https://requests.readthedocs.io/)
- 🔐 [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

## 💡 Dicas Importantes

| Aspecto            | Recomendação                                |
| ------------------ | ------------------------------------------- |
| **Atualizações**   | Diárias é suficiente para maioria dos casos |
| **API**            | RapidAPI é mais acessível que Official API  |
| **Dados Pessoais** | Nunca commit secrets no Git                 |
| **README**         | Mantenha seções atemporais                  |
| **Histórico**      | Git preserva todas as mudanças              |

---

## ❓ Perguntas Frequentes

**P: Posso mudar a frequência de atualização?**
R: Sim! Edit `.github/workflows/sync-linkedin.yml` e mude a cron expression.
Exemplo: `- cron: '0 */6 * * *'` (a cada 6 horas)

**P: Preciso de internet para rodar?**
R: Sim, para buscar dados do LinkedIn. Modo offline usa apenas dados locais.

**P: Posso deletar histórico de commits?**
R: Sim, mas perde histórico. Use: `git reset --hard <commit>`

---

**Última atualização**: Dezembro 2024
