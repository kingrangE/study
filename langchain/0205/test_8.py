""" 
프롬프트 템플릿에 대해 다룹니다.

기존에는 Human Message에 해당 되는 부분만 다루었으나 이곳에선 System Message까지 설정하는 방식을 다룹니다.
"""
from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate,SystemMessagePromptTemplate

# 2-tuple 형식을 이용하여 SystemMessage와 HumanMessage 구분
prompt = ChatPromptTemplate.from_messages([
    ("system","You're kindness AI. you have to answer kindly"),
    ("human", "{input}"),
])

print(prompt.format(input="어떻게 인생을 살아가야 할까요?"))

""" 출력 결과
System: You're kindness AI. you have to answer kindly
Human: 어떻게 인생을 살아가야 할까요?
"""
# HumanMessagePromptTemplate, SystemMessageTemplate을 활용하여 구분
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("You're kindness AI. You have to answer kindly"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

print(prompt.format(input="나이 26살에 대학생이면 나이 많은건가요?"))

""" 출력 결과
System: You're kindness AI. You have to answer kindly
Human: 나이 26살에 대학생이면 나이 많은건가요?
"""