"""
Punto de entrada de FastAPI para el backend.
Define el endpoint POST /ask para recibir preguntas y devolver respuestas generadas por el agente de IA.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import SmartAgent
from app.config import get_settings

app = FastAPI()
settings = get_settings()
agent = SmartAgent(settings.OPENAI_API_KEY)

class AskRequest(BaseModel):
    question: str
    url: str

@app.post("/ask")
def ask(request: AskRequest):
    try:
        answer = agent.answer_question(request.url, request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
