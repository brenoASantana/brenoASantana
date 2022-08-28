#!/bin/bash
# Script para testar os workflows localmente (opcional)
# Use este script para validar o script Python sem GitHub Actions

# Instalar dependências
pip install requests

# Executar script de atualização
export GITHUB_USERNAME="brenoASantana"
python .github/scripts/update-readme.py

echo "✅ Teste concluído!"
echo "Se nenhum erro apareceu, o script funciona corretamente."
echo ""
echo "Próximos passos:"
echo "1. Faça um push das mudanças"
echo "2. Vá para Actions no seu repositório"
echo "3. Veja os workflows rodando automaticamente"
