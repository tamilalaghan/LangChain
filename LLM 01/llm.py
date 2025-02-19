from langchain_openai import OpenAI
import os


class OpenAIConnect:
    def __init__(self):
        pass
    def askgpt(self):
        prompt = input("Ask your question : ")
        if(len(prompt) > 5):
            llm = OpenAI()
            response = llm.invoke(prompt)
            print(f"Response from AI : {response.strip()}")
        else:
            self.askgpt()

gpt = OpenAIConnect()
gpt.askgpt()
        


