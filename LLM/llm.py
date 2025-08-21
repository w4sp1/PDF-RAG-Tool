from langchain_ollama import OllamaLLM

class LLM:
    def __init__(self):
        self.llm = OllamaLLM(model="llama3.2:3b")

    def generate_response(self, prompt):
        for chunk in self.llm.stream(prompt):
            yield chunk
