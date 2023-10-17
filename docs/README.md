## Схема 1 на языке mermaid:

```mermaid
graph TD
    A["Client Web/App"] -->|"HTTP/HTTPS"| B["API FastAPI"]
    B -->|"API Calls"| C["Service A (SQL DB)"]
    B -->|"API Calls"| D["Service B (MongoDB)"]
    B -->|"API Calls"| E["Service C (OpenAI)"]
```

Здесь клиент ("Client Web/App") соединяется с API ("API FastAPI") через HTTP или HTTPS. 
Затем API перенаправляет запросы к различным службам ("Service A", "Service B", "Service C") через API вызовы.

---

## Схема 3 на языке mermaid:

```mermaid
graph TD
    WebClient["Web Client"] -->|HTTP/HTTPS| API["API (FastAPI)"]
    AppClient["App Client (PyQt6)"] -->|HTTP/HTTPS| API
    TgBot["Telegram Bot"] -->|HTTP/HTTPS| API
    AndroidClient["Android App "] -->|HTTP/HTTPS| API
    
    API -->|REST| SQLService["Service A (SQL DB)"]
    API -->|REST| MongoService["Service B (MongoDB)"]
    API -->|REST| OpenAIService["Service C (OpenAI)"]
    API -->|REST| LocalLLM["LLM (Local Server)"]
```

---

## Схема 4 на языке mermaid:

```mermaid
graph TD
    WebClient["Web Client"] -->|HTTP/HTTPS| Docker
    AppClient["App Client (PyQt6)"] -->|HTTP/HTTPS| Docker
    TgBot["Telegram Bot"] -->|HTTP/HTTPS| Docker
    AndroidClient["Android App "] -->|HTTP/HTTPS| Docker

    Docker["Docker Container"] -->|Proxy| API["API (FastAPI)"]

    API -->|REST| SQLService["Service A (SQL DB)"]
    API -->|REST| MongoService["Service B (MongoDB)"]
    API -->|REST| OpenAIService["Service C (OpenAI)"]
    API -->|REST| LocalLLM["LLM (Local Server)"]
```

---

### Ex.1

```stl
solid cube_corner
  facet normal 0.0 -1.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 1.0 0.0 0.0
    endloop
  endfacet
  facet normal -1.0 0.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 0.0 1.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.577 0.577 0.577
    outer loop
      vertex 1.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
endsolid
```
---

## Схема 3 на языке mermaid:

```mermaid
graph TD
    WebClient["Web Client"] -->|HTTP/HTTPS| API
    AppClient["App Client (PyQt6)"] -->|HTTP/HTTPS| API
    TgBot["Telegram Bot"] -->|HTTP/HTTPS| API
    AndroidClient["Android App "] -->|HTTP/HTTPS| API

    API["API (FastAPI)"] -->|Proxy| Docker["Docker Container"]

    API -->|REST| SQLService["Service A (SQL DB)"]
    API -->|REST| MongoService["Service B (MongoDB)"]
    API -->|REST| OpenAIService["Service C (OpenAI)"]
    API -->|REST| LocalLLM["LLM (Local Server)"]
```


```mermaid
graph TD
    WebClient["Web Client"] -->|HTTP/HTTPS| Docker
    AppClient["App Client (PyQt6)"] -->|HTTP/HTTPS| Docker
    TgBot["Telegram Bot"] -->|HTTP/HTTPS| Docker
    AndroidClient["Android App "] -->|HTTP/HTTPS| Docker

    Docker["Docker Container"] -->|Proxy| API["API (FastAPI)"]

    API -->|REST| SQLService["Service A (SQL DB)"]
    API -->|REST| MongoService["Service B (MongoDB)"]
    API -->|REST| OpenAIService["Service C (OpenAI)"]
    API -->|REST| LocalLLM["LLM (Local Server)"]
```
