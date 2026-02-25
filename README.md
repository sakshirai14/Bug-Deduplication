# Bug-Deduplication
An AI-powered Bug Deduplication System that automatically detects and clusters duplicate bug reports using Natural Language Processing (NLP), Machine Learning, and Vector Similarity Search. This system helps QA and engineering teams reduce redundant issue tracking, improve triaging efficiency, and accelerate resolution time.

#🚀Problem Statement
In large-scale software projects, multiple users often report the same issue in slightly different ways. Manually identifying duplicate bug reports:
Wastes developer time
Delays triaging
Creates cluttered issue logs
Impacts sprint planning
This system intelligently identifies semantically similar bug reports even when the wording differs.

#🧠Solution Overview
The system leverages:
Text preprocessing & normalization
Embedding generation using transformer models
Vector similarity search
Clustering for grouping related issues
REST APIs for ingestion & retrieval
Streamlit UI for interactive uploads

#🛠️Tech Stack
Backend: Python, FastAPI
ML/NLP: Scikit-learn, Transformers
Vector Store: FAISS / Custom Vector Store
Frontend: Streamlit
Data Handling: Pandas, JSON
Optional Enhancements: OpenAI embeddings, SentenceTransformers

#⚙️ eatures
✔ Upload bug reports via CSV, Excel, or JSON
✔ Automatic duplicate detection using semantic similarity
✔ Configurable similarity threshold
✔ Vector database storage
✔ Cluster-based grouping of related issues
✔ REST APIs for integration
✔ User-friendly UI for QA teams
