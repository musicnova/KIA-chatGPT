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


## Схема 2 на языке mermaid:

```mermaid
graph TD
    WebClient["Web Client"] -->|HTTP/HTTPS| API["API (FastAPI)"]
    AppClient["App Client"] -->|HTTP/HTTPS| API
    DesktopClient["Desktop App"] -->|HTTP/HTTPS| API
    
    API -->|API Calls| SQLService["Service A (SQL DB)"]
    API -->|API Calls| MongoService["Service B (MongoDB)"]
    API -->|API Calls| OpenAIService["Service C (OpenAI)"]
    API -->|API Calls| LocalLLM["Local LLM"]
```

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
