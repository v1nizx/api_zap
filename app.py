from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
import pywhatkit as wa
import time
from datetime import datetime, timedelta
from typing import Optional
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="WhatsApp Bot API",
    description="API para envio de mensagens no WhatsApp",
    version="1.0.0"
)

# Modelos Pydantic
class MensagemModel(BaseModel):
    numero: str
    mensagem: str
    
class MensagemAgendadaModel(BaseModel):
    numero: str
    mensagem: str
    hora: int
    minuto: int

class MensagemGrupoModel(BaseModel):
    grupo_id: str
    mensagem: str

# Endpoints
@app.get("/")
def home():
    """Endpoint de boas-vindas"""
    return {
        "message": "WhatsApp Bot API",
        "version": "1.0.0",
        "endpoints": {
            "/enviar": "Enviar mensagem instantânea",
            "/agendar": "Agendar mensagem",
            "/grupo": "Enviar mensagem para grupo",
            "/docs": "Documentação completa"
        }
    }

@app.get("/zap")
def envia_msg(numero: str, msg: str) -> dict:
    """Envia mensagem instantânea (mantido para compatibilidade)"""
    try:
        wa.sendwhatmsg_instantly(numero, msg)
        logger.info(f"Mensagem enviada para {numero}")
        return {"status": "Mensagem enviada com sucesso", "numero": numero}
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao enviar mensagem: {str(e)}")

@app.post("/enviar")
def enviar_mensagem(mensagem: MensagemModel):
    """Envia mensagem instantânea via POST"""
    try:
        # Adiciona +55 se não estiver presente
        numero = mensagem.numero
        if not numero.startswith('+'):
            numero = f"+55{numero}"
        
        wa.sendwhatmsg_instantly(numero, mensagem.mensagem)
        logger.info(f"Mensagem enviada para {numero}")
        
        return {
            "status": "sucesso",
            "mensagem": "Mensagem enviada com sucesso",
            "numero": numero,
            "conteudo": mensagem.mensagem,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao enviar mensagem: {str(e)}")

@app.post("/agendar")
def agendar_mensagem(mensagem: MensagemAgendadaModel):
    """Agenda uma mensagem para ser enviada em horário específico"""
    try:
        # Adiciona +55 se não estiver presente
        numero = mensagem.numero
        if not numero.startswith('+'):
            numero = f"+55{numero}"
        
        wa.sendwhatmsg(numero, mensagem.mensagem, mensagem.hora, mensagem.minuto)
        logger.info(f"Mensagem agendada para {numero} às {mensagem.hora}:{mensagem.minuto}")
        
        return {
            "status": "sucesso",
            "mensagem": "Mensagem agendada com sucesso",
            "numero": numero,
            "conteudo": mensagem.mensagem,
            "horario": f"{mensagem.hora:02d}:{mensagem.minuto:02d}",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Erro ao agendar mensagem: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao agendar mensagem: {str(e)}")

@app.post("/grupo")
def enviar_para_grupo(mensagem: MensagemGrupoModel):
    """Envia mensagem para um grupo do WhatsApp"""
    try:
        wa.sendwhatmsg_to_group_instantly(mensagem.grupo_id, mensagem.mensagem)
        logger.info(f"Mensagem enviada para o grupo {mensagem.grupo_id}")
        
        return {
            "status": "sucesso",
            "mensagem": "Mensagem enviada para o grupo com sucesso",
            "grupo_id": mensagem.grupo_id,
            "conteudo": mensagem.mensagem,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem para grupo: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao enviar mensagem para grupo: {str(e)}")

@app.post("/enviar-multiplos")
def enviar_para_multiplos(numeros: list[str], mensagem: str):
    """Envia a mesma mensagem para múltiplos números"""
    resultados = []
    
    for numero in numeros:
        try:
            # Adiciona +55 se não estiver presente
            if not numero.startswith('+'):
                numero = f"+55{numero}"
            
            wa.sendwhatmsg_instantly(numero, mensagem)
            resultados.append({
                "numero": numero,
                "status": "sucesso"
            })
            logger.info(f"Mensagem enviada para {numero}")
            
            # Pequena pausa entre envios
            time.sleep(2)
            
        except Exception as e:
            resultados.append({
                "numero": numero,
                "status": "erro",
                "erro": str(e)
            })
            logger.error(f"Erro ao enviar para {numero}: {str(e)}")
    
    return {
        "status": "processado",
        "total_envios": len(numeros),
        "resultados": resultados,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/status")
def status():
    """Verifica o status da API"""
    return {
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "mensagem": "WhatsApp Bot está funcionando"
    }