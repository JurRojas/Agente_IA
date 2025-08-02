"""
Lógica del agente: carga una URL usando WebBaseLoader y responde preguntas usando LangChain + OpenAI.
"""
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAI
import os

class SmartAgent:
    def __init__(self, openai_api_key: str):
        self.llm = OpenAI(openai_api_key=openai_api_key)

    def load_url(self, url: str):
        """Carga el contenido de una URL usando WebBaseLoader."""
        loader = WebBaseLoader(url)
        docs = loader.load()
        return docs

    def answer_question(self, url: str, question: str) -> str:
        """Genera una respuesta usando el contexto de la URL y la pregunta."""
        docs = self.load_url(url)
        context = " ".join([doc.page_content for doc in docs])
        prompt = f"Contexto: {context}\n\nPregunta: {question}\nRespuesta: "
        return self.llm(prompt)
