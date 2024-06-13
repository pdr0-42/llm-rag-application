RAG-Service
==============================

A service with retrieve-and-generate (RAG) functionality using FastAPI.

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── app
    │   ├── __init__.py
    │   │
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── endpoints
    │   │   │   ├── __init__.py
    │   │   │   └── rag.py          <- Endpoints for RAG
    │   │   └── dependencies.py     <- Dependencies for the API
    │   │
    │   ├── core
    │   │   ├── __init__.py
    │   │   └── config.py           <- Project settings
    │   │
    │   ├── models
    │   │   ├── __init__.py
    │   │   └── rag_pipeline.py     <- RAG pipeline implementation
    │   │
    │   ├── services
    │   │   ├── __init__.py
    │   │   └── rag_service.py      <- Service using the RAG pipeline
    │   │
    │   ├── utils
    │   │   ├── __init__.py
    │   │   └── data_processing.py  <- Data processing functions
    │   │
    │   └── main.py                 <- FastAPI application entry point
    │
    ├── tests                       <- Unit tests for the project
    │   ├── __init__.py
    │   ├── test_data_processing.py <- Tests for data processing
    │   ├── test_rag_pipeline.py    <- Tests for RAG pipeline
    │   └── test_rag_service.py     <- Tests for RAG service
    │
    ├── .gitignore                  <- Files and directories to ignore in Git
    ├── requirements.txt            <- The requirements file for reproducing the analysis environment
    ├── setup.py                    <- Makes the project pip installable (pip install -e .)
    

