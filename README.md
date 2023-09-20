# Personal Document Chatbot

This is a tool that allows users to chat with their personal documents (PDF and TXT) using large language models (LLMs) like GPT and Claude. The tool supports retrieval augmented generation (RAG), multi-document conversational QA, and dynamic text chunking.

## Components

The tool consists of the following components:

1. Document Reader: This component is responsible for reading the user’s documents and converting them into a format that can be processed by the LLMs. It also handles the file management and storage of the documents.
   - File Saver: This subcomponent saves the converted text files into a database or a folder. It also assigns a unique ID to each document for easy retrieval.
   - Document Chunker: This subcomponent splits the documents into smaller chunks of text that can be fed into the LLMs. It also dynamically adjusts the size and position of the chunks based on the user’s queries and the LLM’s responses.
     - Chunk Generator: This subcomponent generates the initial chunks of text from the documents using a sliding window technique. It uses a fixed or variable window size and a stride parameter to determine how much to overlap between adjacent chunks.
     - Chunk Selector: This subcomponent selects the most relevant chunks of text for each query using a similarity measure, such as TF-IDF or BM25. It ranks the chunks based on their similarity scores and returns the top-k chunks for each document.
2. Language Model: This component is responsible for generating responses to the user’s queries. It uses large language models (LLMs) like GPT and Claude to generate natural language responses.
   - RAG: This subcomponent retrieves relevant chunks of text from the user’s documents and uses them to augment the generation of the LLMs.
   - Multi-document Conversational QA: This subcomponent answers questions that require information from multiple documents.
   
## Usage

To use the tool, follow these steps:

1. Save your documents in the `storage` folder.
2. Run the `main.py` script.
3. Enter your query in the console.
4. The tool will generate a response based on your query and the contents of your documents.

## Requirements

The tool requires the following Python packages:

- `torch`
- `transformers`
- `scikit-learn`
- `numpy`