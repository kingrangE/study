
"""
ChatPromptTemplate에서 Prompt Template 결합
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

gpt = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()
#지시, 예시, 맥락을 각각 template을 만들고 합치겠습니다.

instruction = "{product}에 대한 자세한 퍼포먼스 마케팅 계획을 안내해주세요."
example = "예를 들어, 시계에 대한 자세한 퍼포먼스 마케팅 계획은 30-40대를 대상으로 SNS 광고를 하는 등의 계획을 알려주시면 됩니다."
context = "해당 {product}는 {feature}를 특징으로 갖고 있습니다. 이 점을 참고해주세요."

full_template = ChatPromptTemplate.from_template(
    instruction+example+context
)
# 이 방식 외에도 3가지 prompt 중 하나를 PromptTemplate 클래스로 만들면, +로도 full_template을 만들 수 있습니다.
"""예시
instruction = ChatPromptTemplate.from_template("{product}에 대한 자세한 퍼포먼스 마케팅 계획을 안내해주세요.")
example = "예를 들어, 시계에 대한 자세한 퍼포먼스 마케팅 계획은 30-40대를 대상으로 SNS 광고를 하는 등의 계획을 알려주시면 됩니다."
context = "해당 {product}는 {feature}를 특징으로 갖고 있습니다. 이 점을 참고해주세요."

full_template = (instruction+example+context)
"""

#result = full_template.format()

chain = full_template|gpt|output_parser

print(chain.invoke({"product":"AI 서비스","feature":"일반적인 하나의 서비스만 다루는 것이 아닌 생산성 향상, 퀀트 투자, 이미지 생성 등의 다양한 분야를 다룹니다."})) #이미 result에서 template을 완성시켰으므로 그냥 invoke합니다.

""" 결과 
AI 서비스의 퍼포먼스 마케팅 계획은 다양한 서비스군을 포괄하므로, 분야별로 접근 방식을 다르게 해야 합니다. 아래는 생산성 향상, 퀀트 투자, 이미지 생성 등 주요 분야에 대한 세부적인 퍼포먼스 마케팅 계획입니다.

### 1. 생산성 향상 서비스

#### 타겟 오디언스
- 연령대: 25-45세
- 직업: 직장인, 창업가, 프리랜서
- 관심사: 효율성, 시간 관리, 자기계발

#### 채널 및 전략
- **SNS 광고**: LinkedIn, Facebook, Instagram을 통해 타겟 광고 진행. 직장인 및 창업가를 겨냥한 콘텐츠 생성.
- **콘텐츠 마케팅**: 블로그 및 유튜브에 효율성 제고, 시간 관리 기법 관련 글이나 비디오 제작.
- **리타게팅 광고**: 웹사이트 방문자에게 재타겟팅 광고를 통해 재참여 유도.
- **웹 세미나**: 무료 온라인 세미나를 개최하여 서비스를 시연하고 실질적인 예제 공유.

### 2. 퀀트 투자 서비스

#### 타겟 오디언스
- 연령대: 30-50세
- 직업: 투자자, 금융업 종사자, 데이터 애널리스트
- 관심사: 투자 수익, 금융 데이터 분석, 최신 투자 트렌드

#### 채널 및 전략
- **전문 커뮤니티 광고**: Reddit의 투자 관련 서브레딧, 투자 관련 포럼에 광고 게재.
- **SEO 최적화**: 투자 관련 키워드에 대한 블로그 콘텐츠 생성 및 검색 엔진 최적화.
- **유튜브 및 웨비나**: 퀀트 투자 기법 및 성공 사례를 다룬 교육 자료 제작.
- **이메일 마케팅**: 타겟 오디언스를 위한 맞춤형 뉴스레터 발송.

### 3. 이미지 생성 서비스

#### 타겟 오디언스
- 연령대: 20-40세
- 직업: 디자이너, 마케팅 전문가, 콘텐츠 제작자
- 관심사: 디자인, 콘텐츠 제작, 비주얼 아이디어

#### 채널 및 전략
- **비주얼 플랫폼 광고**: Instagram, Pinterest, Behance와 같은 플랫폼에 광고 배치.
- **사용자 생성 콘텐츠 (UGC)**: 사용자들이 생성한 이미지나 디자인을 활용하여 소셜 미디어에서 공유하도록 유도.
- **인플루언서 마케팅**: 디자인 및 콘텐츠 제작 관련 인플루언서와의 협업을 통해 브랜드 인지도 증대.
- **체험 마케팅**: 무료 체험판 제공 및 SNS 이벤트 개최.

### 마케팅 성과 측정 및 최적화

각 서비스 구현 후, 아래의 KPI를 설정하여 성과를 측정하고 최적화합니다.

- **전환율 (Conversion Rate)**: 광고 클릭 후 고객이 최종 행동(구매 등)을 취한 비율.
- **ROI (Return on Investment)**: 광고 비용 대비 수익 계산.
- **웹사이트 트래픽**: 광고 캠페인 후 웹사이트 방문자 수 변화.
- **사용자 피드백**: 고객의 리뷰와 피드백을 통한 서비스 개선 방향 모색.

### 결론

각 분야별로 세심한 타겟팅과 맞춤형 콘텐츠 전략을 세워 효과적인 퍼포먼스 마케팅을 수행할 수 있습니다. 이를 통해 AI 서비스의 인지도와 사용성을 증대시키는 것이 중요합니다.
"""