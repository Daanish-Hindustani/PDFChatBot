from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

#Processes given pdf, embeds, and keeps in a vectorized Data Base
def load_pdf_and_split_text(pdf):
    """
    Loads a PDF document, splits its text into chunks, and returns a list of parsed text chunks.
    Returns:
    - list: List of parsed text chunks.
    """
    loader = PyPDFLoader(f"{pdf}")
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(pages)
    return splits 

def embed_text_splits(splits):
    """
    Embeds the text splits using HuggingFace embeddings and stores them in a vector database.
    Returns:
    - Chroma: Vector database containing the embedded text splits.
    """
    return Chroma.from_documents(documents=splits, embedding=HuggingFaceEmbeddings())

def process_pdf(pdf_path):
    """
    Processes a PDF document by loading, splitting, embedding its text, and storing it in a vector database.
    Returns:
    - Chroma: Vector database containing the embedded text splits.
    """
    pdf_splits = load_pdf_and_split_text(pdf_path)
    vector_data_base = embed_text_splits(pdf_splits)
    return vector_data_base
