(base) m.mohamednadheem@MMOHAMED-NADHEEMS-MacBook-Air langchain-rag % history
 1149  /Users/m.mohamednadheem/opt/anaconda3/bin/python create_database.py
 1150  clear
 1151  pip install --force-reinstall pdfminer.six==20231228
 1152  /Users/m.mohamednadheem/opt/anaconda3/bin/python create_database.py
 1153  /Users/m.mohamednadheem/opt/anaconda3/bin/python query_data.py "What is a correlated subquery?"
 1154   /Users/m.mohamednadheem/opt/anaconda3/bin/python query_data.py "what does the file contain?"
 1155  /usr/bin/python3 /Users/m.mohamednadheem/.vscode/extensions/ms-python.python-2024.14.1-darwin-arm64/python_files/printEnvVariablesToFile.py /Users/m.mohamednadheem/.vscode/extensions/ms-python.python-2024.14.1-darwin-arm64/python_files/deactivate/zsh/envVars.txt
 1156  python create_database.py
 1157  python query_data.py "What is a correlated subquery?"
 1158  clear
 1159  python create_database.py
 1160  clear
 1161  clear
 1162  python create_database.py
 1163  python query_data.py "what is networking commands"
 1164  python query_data.py "what is networking commands.explain in two sentence max"


 # Langchain RAG Tutorial
unchanged content 
## Install dependencies

1. Do the following before installing the dependencies found in `requirements.txt` file because of current challenges installing `onnxruntime` through `pip install onnxruntime`. 

    - For MacOS users, a workaround is to first install `onnxruntime` dependency for `chromadb` using:

    ```python
     conda install onnxruntime -c conda-forge
    ```
    See this [thread](https://github.com/microsoft/onnxruntime/issues/11037) for additonal help if needed. 

     - For Windows users, follow the guide [here](https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file) to install the Microsoft C++ Build Tools. Be sure to follow through to the last step to set the enviroment variable path.


2. Now run this command to install dependenies in the `requirements.txt` file. 

```python
pip install -r requirements.txt
```

3. Install markdown depenendies with: 

```python
pip install "unstructured[md]"
```

## Create database

Create the Chroma DB.

```python
python create_database.py
```

## Query the database

Query the Chroma DB.

```python
python query_data.py "How does Alice meet the Mad Hatter?"
```

> You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.

Here is a step-by-step tutorial video: [RAG+Langchain Python Project: Easy AI/Chat For Your Docs](https://www.youtube.com/watch?v=tcqEUSNCn8I&ab_channel=pixegami).



after changes made in the project 

# Langchain RAG Project

This project implements a Retrieval-Augmented Generation (RAG) system using Langchain and Chroma DB to query documents.

## Features
- Loads PDF and Markdown documents from `data/books` directory
- Creates a vector database using Chroma and HuggingFace embeddings
- Allows semantic search queries against the document database

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create the database:
```bash
python create_database.py
```
This processes documents in `data/books` and creates a Chroma vector database in `chroma/`.

## Usage
Query the database with:
```bash
python query_data.py "Your query text here"
```

Example queries:
```bash
python query_data.py "How does Alice meet the Mad Hatter?"
python query_data.py "Explain nested queries in SQL"
```

## Project Structure
- `create_database.py`: Processes documents and creates Chroma DB
- `query_data.py`: Queries the Chroma DB
- `data/books/`: Contains source documents (PDF/Markdown)
- `chroma/`: Stores the Chroma vector database

## Dependencies
- Langchain
- Chroma DB
- HuggingFace embeddings

## Sample Documents
- Alice in Wonderland (Markdown)
- Database Nested Queries (PDF)
- CCN Record (PDF)
