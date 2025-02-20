from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

class OpenAIChat:
    def __init__(self):
        pass

    def askgpt(self,sysmessage,humanmessage):
        prompt = [
            SystemMessage(content=sysmessage),
            HumanMessage(content=humanmessage)
        ]
        llm = ChatOpenAI()
        response = llm.invoke(prompt)
        print(response.content)


gptchat = OpenAIChat()

print(" Chat with AI ")
role = input("Enter the Role the AI should play : ")
while ( len (role) < 3 ):
    print("Error enter the right role")
    role = input("Enter the Role the AI should play : ")

sysmessage = "You are a "+role

hummessage = input("Enter the question you would like to ask : ")
while ( len (hummessage) < 8 ):
    print("Error enter a valid question")
    hummessage = input("Enter the question you would like to ask : ")

gptchat.askgpt(sysmessage,hummessage)