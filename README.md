# PDFChatBot

# Data Processing
    The pdfProcessing module has three functions which split the PDF text into chunks. The embedding function converts text into a numerical representation. Finally, the vectorized database is a vector that stores all the embeddings. All these functions use LangChain libraries.

# Prompt 
    PdfPrompt.py has three functions which retrieve data and format a prompt for the LLM. The first function (retrieve_documents) takes in search keywords from a question, then embeds them and retrieves n numbers of related documents or text chunks from the vectorized database. The next function (format_documents) takes that output and concatenates them. The final function (make_prompt) creates the prompt that is fed to the LLM.

# Feeding the Llama LLM
    A local Llama was used in this program (see local Llama docs). The primary function in the askllama.py file takes in a PDF and a question, then calls the Data Processing and prompt functions. Then it generates a response by feeding the prompt to the Llama LLM.

# Website
    A Streamlit interface was used to convey this program.
