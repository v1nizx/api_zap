# 🤖 WhatsApp Bot API

Uma API RESTful para envio de mensagens no WhatsApp usando Python, FastAPI e PyWhatKit.

## 🚀 Como usar

### 1. Iniciar o servidor
```bash
./start.sh
```
Ou manualmente:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 2. Acessar a documentação
Abra o navegador em: http://localhost:8000/docs

## 📱 Endpoints disponíveis

### 1. Enviar mensagem instantânea (GET)
```http
GET /zap?numero=5511999999999&msg=Olá, teste!
```

### 2. Enviar mensagem instantânea (POST)
```http
POST /enviar
Content-Type: application/json

{
    "numero": "11999999999",
    "mensagem": "Olá! Esta é uma mensagem de teste."
}
```

### 3. Agendar mensagem
```http
POST /agendar
Content-Type: application/json

{
    "numero": "11999999999",
    "mensagem": "Mensagem agendada!",
    "hora": 14,
    "minuto": 30
}
```

### 4. Enviar para grupo
```http
POST /grupo
Content-Type: application/json

{
    "grupo_id": "ID_DO_GRUPO",
    "mensagem": "Mensagem para o grupo!"
}
```

### 5. Enviar para múltiplos números
```http
POST /enviar-multiplos
Content-Type: application/json

{
    "numeros": ["11999999999", "11888888888"],
    "mensagem": "Mensagem em massa!"
}
```

## 🔧 Exemplos com curl

### Enviar mensagem simples:
```bash
curl -X POST "http://localhost:8000/enviar" \
     -H "Content-Type: application/json" \
     -d '{
       "numero": "11999999999",
       "mensagem": "Olá do bot!"
     }'
```

### Agendar mensagem:
```bash
curl -X POST "http://localhost:8000/agendar" \
     -H "Content-Type: application/json" \
     -d '{
       "numero": "11999999999",
       "mensagem": "Mensagem agendada!",
       "hora": 15,
       "minuto": 30
     }'
```

## 🐍 Exemplos com Python

```python
import requests

# Enviar mensagem
response = requests.post("http://localhost:8000/enviar", json={
    "numero": "11999999999",
    "mensagem": "Olá do Python!"
})
print(response.json())

# Agendar mensagem
response = requests.post("http://localhost:8000/agendar", json={
    "numero": "11999999999",
    "mensagem": "Mensagem agendada!",
    "hora": 16,
    "minuto": 0
})
print(response.json())
```

## ⚠️ Requisitos importantes

1. **WhatsApp Web**: Deve estar logado no navegador
2. **Primeira execução**: O PyWhatKit abrirá o navegador automaticamente
3. **Formato do número**: Use com código do país (+55 para Brasil)
4. **Delay**: Há um pequeno delay entre envios para evitar bloqueios

## 🔐 Formato dos números

- ✅ Correto: `5511999999999` ou `+5511999999999`
- ✅ Correto: `11999999999` (será adicionado +55 automaticamente)
- ❌ Incorreto: `(11) 99999-9999`

## 📋 Status da API

Verifique se a API está funcionando:
```http
GET /status
```

## 🎯 Features

- ✅ Envio instantâneo de mensagens
- ✅ Agendamento de mensagens
- ✅ Envio para grupos
- ✅ Envio em massa
- ✅ Logs detalhados
- ✅ Tratamento de erros
- ✅ Documentação automática (Swagger)
- ✅ Validação de dados com Pydantic

## 🛠️ Tecnologias usadas

- **FastAPI**: Framework web moderno e rápido
- **PyWhatKit**: Biblioteca para automação do WhatsApp
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI
