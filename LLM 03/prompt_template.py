
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate

class ChatwithOpenAI:
    def __init__(self,sysmessage_input, humanmesage_input):
        self.sysmessage_input = sysmessage_input
        self.humanmesage_input = humanmesage_input
    
    def promptTemplate(self):
        sys_message = "You are an {dynamic_sys} expert"
        human_message = "Explain the {dynamic_human} concept in 2 lines"
        prompt_template = ChatPromptTemplate.from_messages([("system",sys_message),("human",human_message)])
        print(f"\n*** Prompt Template ***\n{prompt_template}")
        self.prompt = prompt_template.format_messages(dynamic_sys =  self.sysmessage_input,dynamic_human = self.humanmesage_input)
        print(f"\n*** Prompt ***\n{prompt_template}")
        print(self.prompt)
    
    def initiate_chat(self):
        llm = ChatOpenAI()
        response = llm.invoke(self.prompt)
        print(f"*** Raw Response *** \n{response}")
        print(f"\n\n*** Content  ***\n{response.content}")

# Set Input Variables
sysmessage_input = input("Enter the expertise you require : ")
humanmessage_input = input("Enter the topic you like to request : ")

# Initiate Chat
promptTemplate_instance = ChatwithOpenAI(sysmessage_input, humanmessage_input)
promptTemplate_instance.promptTemplate()
promptTemplate_instance.initiate_chat()
