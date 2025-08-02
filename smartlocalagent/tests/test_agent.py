"""
Prueba unitaria básica para el agente.
"""
import os
import pytest
from app.agent import SmartAgent

@pytest.fixture
def agent():
    api_key = os.getenv("OPENAI_API_KEY", "test-key")
    return SmartAgent(api_key)

def test_load_url(agent):
    docs = agent.load_url("https://www.example.com")
    assert len(docs) > 0
    assert hasattr(docs[0], "page_content")
