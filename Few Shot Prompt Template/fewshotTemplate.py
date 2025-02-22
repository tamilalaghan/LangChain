
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

class ChatwithOpenAI:
    def __init__(self):
        pass
    
    def generateFewShotTemplate(self,sample_dict):
        
        sample_prompt = ChatPromptTemplate.from_messages(
            [
                ("human","{input}"),
                ("ai","{output}")
            ]
        )

        self.fewshot_template = FewShotChatMessagePromptTemplate(
            example_prompt= sample_prompt,
            examples=sample_dict
        )

        print("\n**** Few Shot Template ****")
        print(f"\n{self.fewshot_template}")
        print("\n***Formatted***")
        print(f"\n{self.fewshot_template.format()}")
    
    def generateFinalPrompt(self,system_input,user_input):
        prompt_template = ChatPromptTemplate.from_messages(
           [
            ("system","You are a {system_input} expert"),
            self.fewshot_template,
            ("human","{user_input}")
           ])
        print("\n**** Prompt Template ****")
        print(f"\n{prompt_template}")
        self.prompt = prompt_template.format_messages(system_input= system_input, user_input = user_input)
        print("\n***Formatted Prompt***")
        print(f"\n{self.prompt}")
    
    def initiateChat(self):
        llm = ChatOpenAI()
        response = llm.invoke(self.prompt)
        print("\n**** UnFormatted Response ****")
        print(f"\n{response}")
        print("\n**** Response Content****")
        print(f"\n{response.content}")
        

samples = [
    {"input":"Madam","output":"yes"},
    {"input":"level","output":"yes"},
    {"input":"dad","output":"yes"},
    {"input":"mom","output":"yes"},
    {"input":"reviver","output":"yes"},
    {"input":"revitver","output":"no"},
    {"input":"predator","output":"no"},
    {"input":"mirroe","output":"no"}
    
]


# Instance
fewshot_instance = ChatwithOpenAI()
fewshot_instance.generateFewShotTemplate(samples)
program_input = input("Enter the Number for which AI can predict the answer : ")
fewshot_instance.generateFinalPrompt("puzzle",program_input)
fewshot_instance.initiateChat()