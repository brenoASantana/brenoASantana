#!/usr/bin/env python3
"""
Script para atualizar automaticamente a seção de Projetos Recentes no README
com dados da API do GitHub
"""

import re
import requests
from datetime import datetime

GITHUB_USERNAME = "brenoASantana"
README_FILE = "README.md"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

def fetch_repositories():
    """Busca repositórios do GitHub API"""
    try:
        response = requests.get(
            GITHUB_API_URL,
            params={
                "sort": "updated",
                "direction": "desc",
                "per_page": 6,
                "type": "public"
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar repositórios: {e}")
        return []

def generate_projects_table(repos):
    """Gera a tabela de projetos em formato Markdown"""
    if not repos:
        return "| Projeto | Descrição | URL |\n|---------|-----------|-----|\n"

    table = "| Projeto | Descrição | URL |\n|---------|-----------|-----|\n"

    for repo in repos[:5]:  # Top 5 repositórios recentes
        name = repo.get("name", "")
        description = repo.get("description", "Sem descrição")

        # Limitar descrição a 50 caracteres
        if description and len(description) > 50:
            description = description[:47] + "..."
        elif not description:
            description = "Sem descrição"

        url = repo.get("html_url", "")

        table += f"| **[{name}]({url})** | {description} | [Acessar →]({url}) |\n"

    return table

def update_readme(new_table):
    """Atualiza o README com a nova tabela de projetos"""
    try:
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        # Padrão para encontrar a seção de projetos
        pattern = r"(<!-- PROJETOS_RECENTES_START -->)(.*?)(<!-- PROJETOS_RECENTES_END -->)"

        new_content = re.sub(
            pattern,
            f"\\1\n{new_table}\\3",
            content,
            flags=re.DOTALL
        )

        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(new_content)

        print("✅ README atualizado com sucesso!")
        return True
    except FileNotFoundError:
        print("❌ README.md não encontrado")
        return False
    except Exception as e:
        print(f"❌ Erro ao atualizar README: {e}")
        return False

def main():
    print(f"🔍 Buscando repositórios de {GITHUB_USERNAME}...")
    repos = fetch_repositories()

    if not repos:
        print("❌ Nenhum repositório encontrado")
        return

    print(f"📦 Encontrados {len(repos)} repositórios")
    print("📝 Gerando tabela de projetos...")
    table = generate_projects_table(repos)

    print("✏️ Atualizando README.md...")
    if update_readme(table):
        print("🎉 Atualização concluída!")
    else:
        print("❌ Falha na atualização")

if __name__ == "__main__":
    main()
