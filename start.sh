#!/bin/bash

# Script para iniciar o WhatsApp Bot

echo "🚀 Iniciando WhatsApp Bot API..."
echo "📱 Certifique-se de que o WhatsApp Web está logado no seu navegador"
echo ""

# Ativar ambiente virtual se existir
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✅ Ambiente virtual ativado"
fi

# Verificar se as dependências estão instaladas
echo "📦 Verificando dependências..."
python -c "import fastapi, pywhatkit, uvicorn" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Dependências OK"
else
    echo "❌ Instalando dependências..."
    pip install -r requirements.txt
fi

echo ""
echo "🌐 Iniciando servidor na porta 8000..."
echo "📖 Documentação disponível em: http://localhost:8000/docs"
echo "🔗 API disponível em: http://localhost:8000"
echo ""
echo "Para parar o servidor, pressione Ctrl+C"
echo ""

# Iniciar o servidor
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
