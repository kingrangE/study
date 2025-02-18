# openai basic test
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

llm = ChatOpenAI(
    temperature=0.6, # 창의성, 무작위성
    model = "gpt-3.5-turbo"
)

question = "인생은 어떻게 살아야할까"

print(llm.invoke(question))
