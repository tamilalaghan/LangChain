from langchain_openai import OpenAI
import os


llm = OpenAI()
prompt = input("Enter the query would you like to pass to OpenAI ? : ")
if( len(prompt) > 5 ):
    print( llm.invoke(prompt))