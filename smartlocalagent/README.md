# SmartLocalAgent

Agente IA local con FastAPI, LangChain y OpenAI, capaz de responder preguntas sobre el contenido de una URL.

## Instalación

1. Clona el repositorio o copia los archivos.
2. Crea un entorno virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Copia `.env.example` a `.env` y coloca tu API Key de OpenAI.

## Uso

1. Ejecuta el backend:
   ```
   uvicorn app.main:app --reload
   ```
2. Abre `frontend/index.html` en tu navegador.

## Pruebas

```
pytest
```

## Docker (opcional)

Puedes construir y correr el contenedor:

```
docker build -t smartlocalagent .
docker run -p 8000:8000 smartlocalagent
```
