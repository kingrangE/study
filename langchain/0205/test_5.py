"""
multi chain
1. first chain : Answer in english
2. second chain : tranlate into korean
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")
answer_prompt = ChatPromptTemplate.from_template("You're a kindness respondent. so you have to answer this question with kindness. Question :{question}")
translate_prompt = ChatPromptTemplate.from_template("You're a good translator. so you have to translate this english content into korean. content : {content}")
output_parser = StrOutputParser()
chain1 = answer_prompt|llm|output_parser
chain2 = (
    {"content" : chain1}
    | translate_prompt
    | llm
    | output_parser
)

output = chain2.invoke({"question":"영어 회화를 잘하기 위한 실용적인 방법 5개를 알려주세요."})
print(output)

"""
result:
당신이 영어 대화 능력을 향상시키기 위한 5가지 실용적인 팁이 있습니다. 

1. 꾸준히 연습하세요: 영어 대화를 포함한 모든 기술을 향상시키는 데 일정한 연습이 중요합니다. 친구, 가족 또는 자신에게 영어로 말하는 것을 최대한 해보세요.

2. 언어에 몰두하세요: 영어 영상물이나 영어 음악, 책 등을 통해 자연스러운 영어 대화 패턴과 어휘에 익숙해지세요.

3. 대화 그룹에 가입하거나 언어 교환 파트너를 찾으세요: 원어민이나 동양소가 교사들과 대화를 나누는 것은 자신감을 얻고 말하기 기술을 향상시키는 데 도움이 됩니다.

4. 흔한 표현과 문장 배우고 사용하세요: 다양한 상황에서 사용할 수 있는 일상적인 표현을 배워 사용하세요. 이렇게 하면 대화가 더 자연스럽고 유창해집니다.

5. 실수를 두려워 말아요: 실수하는 것은 학습 과정의 자연스러운 부분이라는 것을 기억하세요. 이를 향상시키고 언어 능력을 키우는 기회로 삼아야 합니다.

이런 팁들이 당신이 영어 대화 능력을 향상시키는 여정에서 도움이 되길 바랍니다!
"""