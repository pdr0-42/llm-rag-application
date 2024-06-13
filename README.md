rag-service/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   └── rag.py              # Endpoints para RAG
│   │   └── dependencies.py         # Dependências da API
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py               # Configurações do projeto
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── rag_pipeline.py         # Implementação da pipeline RAG
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── rag_service.py          # Serviço que usa a pipeline RAG
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── data_processing.py      # Funções para processamento de dados
│   │
│   └── main.py                     # Ponto de entrada da aplicação FastAPI
│
├── data/
│   ├── raw/                        # Dados brutos
│   ├── processed/                  # Dados processados
│   └── embeddings/                 # Vetores de embeddings
│
├── tests/
│   ├── __init__.py
│   ├── test_data_processing.py     # Testes para processamento de dados
│   ├── test_rag_pipeline.py        # Testes para pipeline RAG
│   └── test_rag_service.py         # Testes para serviço RAG
│
├── .gitignore
├── requirements.txt                # Dependências do projeto
├── README.md                       # Descrição do projeto
└── setup.py                        # Script de instalação
