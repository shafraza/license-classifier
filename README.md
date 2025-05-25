# License Classifier API

## Objective
Classify software licenses into semantic categories using Groq LLM via FastAPI.

## Stack
- FastAPI
- Groq API (Mixtral)
- pandas, openpyxl
- Docker

## API Endpoints
- `GET /licenses`: List all classified licenses.
- `GET /summary`: Summary of categories.
- `PUT /licenses/{id}`: Update and mark as validated.

## Local Setup

pip install -r requirements.txt
uvicorn main:app --reload



## **Next Strategy for Scaling**

- **Scaling to 10K licenses/day**:
  - Batch requests and use async pipelines.
  - Use a vector DB + retrieval-augmented generation (RAG) to avoid overloading the LLM.
  - Parallel inference via job queues (Celery + Redis).
- **Embeddings**:
  - Encode license description with `text-embedding-3-small`, cluster/classify using cosine similarity + a lightweight classifier.


