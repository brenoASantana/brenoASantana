#!/usr/bin/env python3
"""
Script para sincronizar informações do LinkedIn com README.md
Atualiza a data de última sincronização e informações do perfil

Configuração:
- LINKEDIN_PROFILE_ID: ID ou username do perfil (ex: brenoasantana)
- RAPIDAPI_KEY: Chave da API RapidAPI (opcional, para versão com dados reais)
"""

import os
import re
import json
from datetime import datetime, timezone
from pathlib import Path

# Tente importar requests se disponível
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


class LinkedInSync:

    def __init__(self, profile_id: str = "brenoasantana"):
        self.profile_id = profile_id
        self.readme_path = Path("README.md")
        self.profile_url = f"https://www.linkedin.com/in/{profile_id}/"

    def get_linkedin_data(self):
        """
        Busca dados do LinkedIn

        OPÇÃo 1: API Oficial do LinkedIn (requer aprovação)
        OPÇÃo 2: RapidAPI LinkedIn endpoints
        OPÇÃo 3: Dados estáticos (padrão atual)
        """

        # Versão padrão: retorna dados estruturados
        data = {
            'profile_url': self.profile_url,
            'last_updated': self.get_timestamp(),
            'profile_verified': True,
            'profile_id': self.profile_id
        }

        # Se deseja dados reais, descomente e configure RAPIDAPI_KEY
        # data.update(self._fetch_from_rapidapi())

        return data

    def _fetch_from_rapidapi(self):
        """
        Busca dados reais do LinkedIn via RapidAPI

        Requer:
        - RAPIDAPI_KEY nas variáveis de ambiente
        - Acesso à API linkedin-data2

        Link: https://rapidapi.com/linkedin-data-linkedin-data-default/api/linkedin-data2
        """

        if not HAS_REQUESTS:
            print("⚠️  Requests não instalado. Usando dados padrão.")
            return {}

        api_key = os.getenv("RAPIDAPI_KEY")
        if not api_key:
            print("ℹ️  RAPIDAPI_KEY não configurada. Usando dados padrão.")
            return {}

        try:
            url = "https://linkedin-data2.p.rapidapi.com/get-profile-data"
            headers = {
                "X-RapidAPI-Key": api_key,
                "X-RapidAPI-Host": "linkedin-data2.p.rapidapi.com"
            }

            params = {
                "linkedin_url": self.profile_url,
                "include_skills": "true"
            }

            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            return {
                'headline': data.get('headline', ''),
                'about': data.get('about', ''),
                'skills': data.get('skills', []),
                'certifications': data.get('certifications', []),
            }

        except Exception as e:
            print(f"⚠️  Erro ao buscar dados do LinkedIn: {e}")
            return {}

    def get_timestamp(self):
        """Retorna timestamp formatado em português"""
        now = datetime.now(timezone.utc)
        return now.strftime('%d de %B de %Y')

    def update_readme(self, linkedin_data):
        """
        Atualiza o README com informações do LinkedIn
        """

        if not self.readme_path.exists():
            print(f"❌ Arquivo {self.readme_path} não encontrado!")
            return False

        with open(self.readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Criar badge com timestamp
        timestamp_br = linkedin_data['last_updated']

        # Seção de sincronização
        sync_section = (
            f"---\n\n"
            f"> ✨ **Dados Sincronizados com LinkedIn**\n"
            f"> Este README é mantido atualizado automaticamente.\n"
            f"> [Acesse meu LinkedIn](https://www.linkedin.com/in/brenoasantana/) para detalhes completos.\n"
            f"> Última sincronização: {timestamp_br}\n"
        )

        # Verificar se seção já existe
        if "Dados Sincronizados com LinkedIn" in content:
            # Atualizar apenas o timestamp
            pattern = r"(> Última sincronização:) .*"
            new_line = f"\\1 {timestamp_br}"
            content = re.sub(pattern, new_line, content)
        else:
            # Inserir seção antes das Habilidades Técnicas
            if "## 💻 Habilidades Técnicas" in content:
                content = content.replace(
                    "## 💻 Habilidades Técnicas",
                    sync_section.rstrip() + "\n\n## 💻 Habilidades Técnicas"
                )

        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("✅ README atualizado com sucesso!")
        print(f"📅 Última sincronização: {timestamp_br}")
        return True

    def run(self):
        """Executa a sincronização completa"""
        print("🔄 Iniciando sincronização com LinkedIn...")
        print(f"👤 Perfil: {self.profile_url}")

        try:
            linkedin_data = self.get_linkedin_data()
            success = self.update_readme(linkedin_data)

            if success:
                print("✨ Sincronização concluída!")
                return 0
            else:
                return 1

        except Exception as e:
            print(f"❌ Erro durante sincronização: {e}")
            return 1


def main():
    """Ponto de entrada do script"""

    # Obter ID do perfil das variáveis de ambiente ou padrão
    profile_id = os.getenv("LINKEDIN_PROFILE_ID", "brenoasantana")

    syncer = LinkedInSync(profile_id)
    exit_code = syncer.run()

    exit(exit_code)


if __name__ == '__main__':
    main()

