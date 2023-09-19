## Схема на языке mermaid:

```mermaid
graph TD
    A[Client Web/App] -->|HTTP/HTTPS| B[API FastAPI]
    B -->|API Calls| C[Service A (SQL DB)]
    B -->|API Calls| D[Service B (MongoDB)]
    B -->|API Calls| E[Service C (OpenAI)]
```

Здесь клиент ("Client Web/App") соединяется с API ("API FastAPI") через HTTP или HTTPS. 
Затем API перенаправляет запросы к различным службам ("Service A", "Service B", "Service C") через API вызовы.
