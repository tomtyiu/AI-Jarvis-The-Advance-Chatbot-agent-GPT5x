# Open AI
fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()

# Importing
from openai import OpenAI
from dotenv import load_dotenv

# coding

openai.api_key = API

client = OpenAI()
load_dotenv()
#completion = openai.Completion()

def QuestionAnswer(question,chat_log = None):
    Filelog = open("DataBase\\qna_log.txt","r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {question}\nAnswer :'
    response = client.responses.create(
        model = "gpt-5.2",
        input=prompt,
        tools=[{"type": "web_search"}],
        )
    answer = response.output_text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    Filelog = open("DataBase\\qna_log.txt","w")
    Filelog.write(chat_log_template_update)   
    Filelog.close()
    return answer     
print(QuestionAnswer("What is the capital of India?"))    



