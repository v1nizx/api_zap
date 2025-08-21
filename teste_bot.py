#!/usr/bin/env python3
"""
Exemplo de teste do WhatsApp Bot
Execute este script para testar as funcionalidades do bot
"""

import requests
import json
from datetime import datetime, timedelta

# URL base da API
BASE_URL = "http://localhost:8000"

def test_status():
    """Testa se a API está funcionando"""
    try:
        response = requests.get(f"{BASE_URL}/status")
        print("✅ Status da API:", response.json())
        return True
    except Exception as e:
        print("❌ Erro ao conectar com a API:", str(e))
        return False

def test_enviar_mensagem():
    """Testa o envio de uma mensagem"""
    # IMPORTANTE: Substitua pelo seu número de teste
    numero = "11999999999"  # ⚠️ MUDE PARA SEU NÚMERO!
    
    data = {
        "numero": numero,
        "mensagem": f"🤖 Teste do WhatsApp Bot - {datetime.now().strftime('%H:%M:%S')}"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/enviar", json=data)
        print("📱 Resultado do envio:", response.json())
        return True
    except Exception as e:
        print("❌ Erro ao enviar mensagem:", str(e))
        return False

def test_agendar_mensagem():
    """Testa o agendamento de uma mensagem"""
    # IMPORTANTE: Substitua pelo seu número de teste
    numero = "11999999999"  # ⚠️ MUDE PARA SEU NÚMERO!
    
    # Agenda para 2 minutos no futuro
    now = datetime.now() + timedelta(minutes=2)
    
    data = {
        "numero": numero,
        "mensagem": f"⏰ Mensagem agendada enviada às {now.strftime('%H:%M')}!",
        "hora": now.hour,
        "minuto": now.minute
    }
    
    try:
        response = requests.post(f"{BASE_URL}/agendar", json=data)
        print("⏰ Resultado do agendamento:", response.json())
        return True
    except Exception as e:
        print("❌ Erro ao agendar mensagem:", str(e))
        return False

def main():
    """Função principal de teste"""
    print("🚀 Iniciando testes do WhatsApp Bot")
    print("=" * 50)
    
    # Testa conexão
    if not test_status():
        print("❌ API não está funcionando. Certifique-se de que o servidor está rodando.")
        return
    
    print("\n" + "=" * 50)
    print("IMPORTANTE: Antes de continuar:")
    print("1. Certifique-se de que o WhatsApp Web está logado no navegador")
    print("2. Edite este arquivo e coloque seu número de teste nas funções")
    print("3. O número deve estar no formato: 11999999999 (sem +55)")
    print("=" * 50)
    
    input("Pressione Enter para continuar com os testes...")
    
    # Testa envio de mensagem
    print("\n📱 Testando envio de mensagem...")
    test_enviar_mensagem()
    
    # Testa agendamento
    print("\n⏰ Testando agendamento de mensagem...")
    test_agendar_mensagem()
    
    print("\n✅ Testes concluídos!")
    print("📖 Acesse http://localhost:8000/docs para ver toda a documentação")

if __name__ == "__main__":
    main()
