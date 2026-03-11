# 🚀 Day 4: Building a Mini RAG Pipeline

Welcome to the **Retrieval Augmented Generation (RAG)** workshop! [cite_start]Today, we solve the three greatest "sins" of standard Large Language Models: **Hallucinations**, **Knowledge Cutoffs**, and **Lack of Private Data Access**[cite: 1, 9].

## 🧠 Why RAG?
[cite_start]Standard LLMs like GPT or Claude are powerful, but their knowledge is "frozen" at the time of their last training[cite: 1, 8]. [cite_start]If you ask about a company policy created yesterday, they might guess (hallucinate) or simply not know[cite: 4, 119]. 

**RAG** changes the game by:
1.  [cite_start]**Retrieving** relevant snippets from your own documents[cite: 129].
2.  [cite_start]**Augmenting** the prompt with that specific context[cite: 135].
3.  [cite_start]**Generating** an answer grounded in real, private data[cite: 136, 149].

## 🛠️ Components of This Project
[cite_start]This repository implements the core "Retrieval" logic of a RAG system[cite: 11]:

- [cite_start]**Chunking:** Understanding how to break large documents into manageable pieces (300-800 tokens) so retrieval is precise[cite: 15, 16].
- [cite_start]**Embeddings:** Turning text into mathematical vectors that represent meaning[cite: 156, 157].
- [cite_start]**Semantic Search:** Using similarity scores to find the "closest" document to a user's question[cite: 160].

## 📁 Project Structure
- `semantic_search.py`: The engine that finds relevant information.
- `documents.txt`: Our local knowledge base.
- `queries.txt`: The questions we asked our system.
- `results.txt`: The "Grounded" evidence retrieved by our pipeline.

## 🚀 How to Run
1. Ensure you have `numpy` installed.
2. Add your documents to `documents.txt`.
3. Run the search script:
   ```bash
   python semantic_search.py