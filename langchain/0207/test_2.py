# openai image recognition test
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

llm = ChatOpenAI(
    temperature=0.6, # 창의성, 무작위성
    model = "gpt-4o"
)

url = 'test.jpeg'

answer = llm.stream(url)

print("[ 답변 ]")
for token in answer :
    print(token.content,end= " | ")
