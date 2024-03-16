from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from pdfPrompt import make_prompt

def askllama(pdf, question):
    #Retrives prompt
    prompt = make_prompt(pdf, question)
    #Feeds ollama the prompt
    llm = Ollama(model="llama2:latest", 
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    #gets response from Llama
    return f"ChatBot: {llm.invoke(prompt)}"
    

def main():
    pdf = "morning-market-report.pdf"
    #userPdf = input("Enter PDF Name Please: ")
    question = input("enter question: ")
    userPdf = pdf
    response = askllama(userPdf, question)
    print(response)

if __name__ == "__main__":
    main()