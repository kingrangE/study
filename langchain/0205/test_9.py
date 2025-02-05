"""
few-shot Prompt를 시도합니다.
few-shot Prompt는 몇가지 예시를 전달하는 방식입니다.
"""
from langchain_core.prompts import PromptTemplate,HumanMessagePromptTemplate,AIMessagePromptTemplate,FewShotPromptTemplate

few_shot_template = PromptTemplate(
    input_variables=["question","answer"],
    template="Question :{question}\nAnswer :{answer}"
)

# example은 작성하기 귀찮아서 wikidocs에서 가져왔습니다.
examples = [
    {  "question": "지구의 대기 중 가장 많은 비율을 차지하는 기체는 무엇인가요?",
        "answer": "지구 대기의 약 78%를 차지하는 질소입니다."
    },
    {
        "question": "광합성에 필요한 주요 요소들은 무엇인가요?",
        "answer": "광합성에 필요한 주요 요소는 빛, 이산화탄소, 물입니다."
    },
    {
        "question": "피타고라스 정리를 설명해주세요.",
        "answer": "피타고라스 정리는 직각삼각형에서 빗변의 제곱이 다른 두 변의 제곱의 합과 같다는 것입니다."
    },
    {
        "question": "지구의 자전 주기는 얼마인가요?",
        "answer": "지구의 자전 주기는 약 24시간(정확히는 23시간 56분 4초)입니다."
    },
    {
        "question": "DNA의 기본 구조를 간단히 설명해주세요.",
        "answer": "DNA는 두 개의 폴리뉴클레오티드 사슬이 이중 나선 구조를 이루고 있습니다."
    },
    {
        "question": "원주율(π)의 정의는 무엇인가요?",
        "answer": "원주율(π)은 원의 지름에 대한 원의 둘레의 비율입니다."
    }
]
#방식 1 FewShotPromptTemplate 사용하기
few_shot_prompts = FewShotPromptTemplate(
    examples= examples,
    example_prompt = few_shot_template,
    suffix = "Question : {question}",
    input_variables=["question"]
)

print(few_shot_prompts.invoke({"question":"전길원이 누구인가요?"}))
"""결과
text='Question :지구의 대기 중 가장 많은 비율을 차지하는 기체는 무엇인가요?\nAnswer :지구 대기의 약 78%를 차지하는 질소입니다.\n\n
Question :광합성에 필요한 주요 요소들은 무엇인가요?\nAnswer :광합성에 필요한 주요 요소는 빛, 이산화탄소, 물입니다.\n
\nQuestion :피타고라스 정리를 설명해주세요.\nAnswer :피타고라스 정리는 직각삼각형에서 빗변의 제곱이 다른 두 변의 제곱의 합과 같다는 것입니다.\n
\nQuestion :지구의 자전 주기는 얼마인가요?\nAnswer :지구의 자전 주기는 약 24시간(정확히는 23시간 56분 4초)입니다.\n
\nQuestion :DNA의 기본 구조를 간단히 설명해주세요.\nAnswer :DNA는 두 개의 폴리뉴클레오티드 사슬이 이중 나선 구조를 이루고 있습니다.\n
\nQuestion :원주율(π)의 정의는 무엇인가요?\nAnswer :원주율(π)은 원의 지름에 대한 원의 둘레의 비율입니다.\n
\nQuestion : 전길원이 누구인가요?'
"""