#!/usr/bin/env python3
"""
Script para atualizar o README com os 3 projetos mais recentemente editados
"""

import os
import re
import requests
from datetime import datetime

GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', 'brenoASantana')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')

def get_recent_repos():
    """Busca os 3 repositórios mais recentemente atualizados"""
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'

    url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'
    params = {
        'sort': 'updated',
        'direction': 'desc',
        'per_page': 3,
        'type': 'owner'
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()

def format_repo_table(repos):
    """Formata os repositórios em uma tabela Markdown"""
    table = """## 🚀 Projetos Recentes

| Projeto | Descrição | URL |
|---------|-----------|-----|
"""

    for repo in repos:
        name = repo['name']
        description = repo['description'] or 'Sem descrição'
        url = repo['html_url']

        # Limita a descrição a 50 caracteres
        if len(description) > 50:
            description = description[:47] + '...'

        table += f"| **[{name}]({url})** | {description} | [Acessar →]({url}) |\n"

    table += "\n"
    return table

def update_readme(recent_projects_table):
    """Atualiza o README.md com a tabela de projetos recentes"""

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Padrão para encontrar a seção de projetos recentes (ou criar se não existir)
    projects_pattern = r'(## 📱 Conectar-se Comigo\n\n<div align="center">.*?</div>\n)'

    if re.search(projects_pattern, content, re.DOTALL):
        # Se encontrar a seção de conexão, insere após ela
        content = re.sub(
            projects_pattern,
            r'\1\n' + recent_projects_table,
            content,
            count=1,
            flags=re.DOTALL
        )
    else:
        # Fallback: insere antes das habilidades técnicas
        habilidades_pattern = r'(---\n\n## 💻 Habilidades Técnicas)'
        content = re.sub(
            habilidades_pattern,
            recent_projects_table + r'\1',
            content,
            count=1
        )

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ README atualizado com sucesso!")

def main():
    """Função principal"""
    try:
        print(f"🔍 Buscando 3 repositórios mais recentes de {GITHUB_USERNAME}...")
        repos = get_recent_repos()

        if not repos:
            print("❌ Nenhum repositório encontrado")
            return

        print(f"✨ Encontrados {len(repos)} repositório(s)")

        table = format_repo_table(repos)
        update_readme(table)

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao consultar API: {e}")
        exit(1)
    except Exception as e:
        print(f"❌ Erro ao atualizar README: {e}")
        exit(1)

if __name__ == '__main__':
    main()
