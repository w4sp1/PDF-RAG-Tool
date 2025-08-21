from langchain_community.document_loaders import PyMuPDFLoader
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from LLM.llm import LLM

class Reader:
    def __init__(self, pdfPath, prompt):
        self.prompt = prompt

        self.document = PyMuPDFLoader(pdfPath).load()
        print(len(self.document))
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.llm = LLM()

    def respond(self):
        split_documents = self.text_splitter.split_documents(self.document)
        self.vector_store = FAISS.from_documents(split_documents, OllamaEmbeddings(model="nomic-embed-text"))
        context = self.vector_store.similarity_search(self.prompt, k=4)
        content = " ".join([i.page_content for i in context])
        prompt = "You are a helpful assistant who can read PDF documents and give proper answers to questions on the PDF. You are to ensure your answers are crisp yet detailed enough. If you do not know answers to any questions, respond with 'I don't know'\n. Based on the context given below: \n"+content+"\nAnswer:"+self.prompt

        for i in self.llm.generate_response(prompt):
            yield i



