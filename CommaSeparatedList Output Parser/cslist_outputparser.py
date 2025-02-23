from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.output_parsers.list import ListOutputParser
from langchain.output_parsers import CommaSeparatedListOutputParser

class OutputParserChatGpt:
    def __init__(self):
        pass

    def queryChatGpt(self,start_query,query):

        prompt_template = PromptTemplate(
        template= " {start_query} {query}",
        input_variables=["start_query","query"]
        )
        prompt = prompt_template.format(query=query,start_query=start_query)
        print("**** Query Prompt ****")
        print(prompt)

        llm = OpenAI()
        response = llm.invoke(prompt)
        print("**** Query Response ****")
        print(response)
    
    def queryChatGptParser(self,start_query,query):

       
        ouput_parser = CommaSeparatedListOutputParser()
        fomat_instructions = ouput_parser.get_format_instructions()
        print("**** Format Instructions ****")
        print(fomat_instructions)

        prompt_template = PromptTemplate(
        template= " {start_query} {query} \n {format_ins}",
        input_variables=["start_query","query"],
        partial_variables={"format_ins":fomat_instructions}
        )
        prompt = prompt_template.format(query=query,start_query=start_query)
        print("**** Query Prompt ****")
        print(prompt)

        llm = OpenAI()
        response = llm.invoke(prompt)
        print("**** Query Response ****")
        print(response.strip())
        print(f"Data Type of Response {type(response)}")

        response_list = ouput_parser.parse(response)
        print("**** Response List ****")
        print(response_list)
        print(f"Type of Response List {type(response_list)}")



# alpha = OutputParserChatGpt()
# alpha_start_query = "List 3 "
# alpha_query = input(f"**** User Query ****\n Complete the Query : {alpha_start_query}")
# alpha.queryChatGpt(alpha_start_query,alpha_query)

beta = OutputParserChatGpt()
beta_start_query = "List 3 "
beta_query = input(f"**** User Query ****\n Complete the Query : {beta_start_query}")
beta.queryChatGptParser(beta_start_query,beta_query)