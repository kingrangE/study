
from langchain_core.prompts import ChatPromptTemplate
"""
langchain_core의 prompts 모듈의 ChatPromptTemplate 클래스 사용해보기
"""

prompt = ChatPromptTemplate.from_template("You're an expert in DevOps. Answer the question. <Question>:{input}")
print(prompt)

"""
출력 결과 : 
input_variables=['input'] input_types={} partial_variables={} 
messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], input_types={}, partial_variables={}, template="You're an expert in DevOps. Answer the question. <Question>:{input}"), 
additional_kwargs={})]
"""