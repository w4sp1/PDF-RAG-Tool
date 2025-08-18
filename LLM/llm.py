from langchain_ollama import OllamaLLM

class LLM:
    def __init__(self, prompt):
        self.prompt = prompt
        self.llm = OllamaLLM(model="llama3.2:3b")

    def generate_response(self):
        for chunk in self.llm.stream(self.prompt):
            yield chunk
