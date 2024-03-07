from pdfProcessing import process_pdf
#Creates prompt to feed llama2
def retrieve_documents(pdf, search_type, search_kwargs):
    """
    Searches through the Vector DB and retrieves documents based on search types.

    Parameters:
    - pdf (str): Path to the PDF file.
    - search_type (str): Type of search (e.g., "similarity").
    - search_kwargs (dict): Search arguments used to retrieve a specific number of documents.

    Returns:
    - Retriever: Retriever object for retrieving documents.
    """
    vector_store = process_pdf(pdf)
    return vector_store.as_retriever(search_type=search_type, search_kwargs=search_kwargs)

def format_documents(pages):
    """
    Formats a list of document pages into a single string.

    Parameters:
    - pages (list): List of document pages.

    Returns:
    - str: Formatted string containing document content.
    """
    return "\n\n".join(page.page_content for page in pages)

def make_prompt(pdf, question):
    """
    Creates a prompt for a question-answering task.

    Parameters:
    - pdf (str): Path to the PDF file.

    Returns:
    - str: Prompt for question-answering with context.
    """
    question = question
    retriever_instance = retrieve_documents(pdf, "similarity", {"k": 6})
    retrieved_docs = retriever_instance.invoke(question)
    context = format_documents(retrieved_docs)
    prompt = f"You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.\n" \
             f"Your answer should be detailed and should contain text from the context. If you don't know the answer, just say that you don't know.\n" \
             f"Use three sentences MAXIMUM and keep the answer concise. Also please formate to be readable\n" \
             f"Question: {question}\nContext: {context}\nAnswer: "
    return prompt

def main():
    pdf_path = "morning-market-report"
    question = input("what is your question today: ")
    prompt_text = make_prompt(pdf_path,question)
    print(prompt_text)

if __name__ == "__main__":
    main()

