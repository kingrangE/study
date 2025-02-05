"""invoke, batch, stream of Runnable protocol test"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

gpt = ChatOpenAI(model= "gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template("You're a good teacher in marketing. so you have to give questional to how to sell this service. Question :{question}")

output_parser = StrOutputParser()

chain = prompt|gpt|output_parser

# invoke는 기본 한 개의 답변을 한 번에 받을 때 사용하는 방식

# output = chain.invoke({"question":"I have made ai services. but I don't know how to people know my service. Could you give me a suggestion?"})
# print(output)
""" output:
1. Who is your target audience for your AI services? 
2. What unique value does your AI service provide compared to competitors in the market? 
3. Have you identified the channels through which you can reach your target audience (e.g. social media, email marketing, SEO)? 
4. How are you currently promoting your AI services? 
5. Have you considered partnering with influencers or industry experts to promote your services? 
6. Have you thought about offering a free trial or demo of your AI services to attract potential customers? 
7. Are you leveraging customer testimonials or case studies to showcase the success stories of your AI services? 
8. Have you considered attending industry events or conferences to network and promote your AI services? 
9. How are you tracking the success and ROI of your marketing efforts for your AI services? 
10. What is your overall marketing strategy and budget for promoting your AI services?
"""
# batch는 한 번에 여러개로 질문하는 경우에 사용, 아래는 list comprehension을 사용한 방식

# questions = ["I have made ai services. but I don't know how to people know my service. Could you give me a suggestion?","Im working in cafe. but my cafe isn't famous. How can I make it famous?","I made pencil. how to sell it?"]
# outputs = chain.batch([{"question":q} for q in questions])
# for question,output in zip(questions,outputs):
#     print(f"Q:{question}\nA:{output}")
"""
Q:I have made ai services. but I don't know how to people know my service. Could you give me a suggestion?
A:1. What specific target audience are you trying to reach with your AI services?

2. Have you identified the unique value proposition of your AI services and how they differ from competitors?

3. What marketing channels are you currently utilizing to promote your AI services?

4. Have you considered leveraging social media platforms to increase awareness of your AI services?

5. Have you thought about partnering with influencers or industry experts to endorse your AI services?

6. How are you currently collecting and utilizing customer feedback to improve your AI services and attract new customers?

7. Have you considered hosting webinars or workshops to showcase the benefits of your AI services to potential customers?

8. Are there any industry events or conferences where you could showcase your AI services to a larger audience?

9. How are you utilizing email marketing to keep past customers engaged and informed about new offerings?

10. Have you considered collaborating with other businesses to offer bundled services that complement your AI offerings?
Q:Im working in cafe. but my cafe isn't famous. How can I make it famous?
A:1. Have you identified your target market and customer base? Is there a specific demographic or group of people that your cafe caters to?

2. Have you implemented a marketing strategy to promote your cafe? Are you utilizing social media, local advertising, or other promotional tactics to increase visibility?

3. Have you considered partnering with other local businesses or community events to increase exposure for your cafe?

4. Are you offering unique and innovative menu items or specials that will set your cafe apart from competitors?

5. Are you providing exceptional customer service and creating a welcoming atmosphere to encourage repeat business and positive word-of-mouth recommendations?

6. Have you considered hosting events or promotions at your cafe to attract new customers and engage with the community?

7. Are you actively seeking feedback from customers to make improvements and ensure satisfaction?

8. Have you considered offering delivery or catering services to reach a wider audience and increase revenue opportunities?

9. Have you invested in professional signage and branding for your cafe to create a memorable and consistent image?

10. Have you researched and analyzed the competition in your area to identify opportunities for differentiation and growth in the market?
Q:I made pencil. how to sell it?
A:1. Who is your target market for the pencil? 
2. What sets your pencil apart from others on the market? 
3. How can you convey the benefits of your pencil to potential customers? 
4. What distribution channels will you use to reach your target market? 
5. How will you price your pencil to maximize sales and profitability? 
6. What promotional strategies will you use to generate interest and awareness for your pencil? 
7. How will you handle customer service and feedback to ensure customer satisfaction and repeat business? 
8. How will you measure the success of your sales efforts for the pencil?
"""

output = chain.stream({"question":"I have made ai services. but I don't know how to people know my service. Could you give me a suggestion?"})
for chunk in output :
    print(chunk,end = " | ",flush=True) # flush = stream 된 결과를 출력하게 해주는 것, flush = False로 설정하게 되면, 대기 후, 한 번에 출력됩니다.

"""
 | Here |  are |  some |  questions |  you |  can |  ask |  yourself |  to |  help |  promote |  your |  AI |  services | :

 | 1 | . |  Who |  is |  your |  target |  audience |  for |  the |  AI |  services |  you |  have |  created | ?
 | 2 | . |  What |  specific |  problems |  or |  pain |  points |  do |  your |  services |  address |  for |  potential |  customers | ?
 | 3 | . |  How |  is |  your |  AI |  service |  different |  or |  better |  than |  what |  is |  currently |  available |  on |  the |  market | ?
 | 4 | . |  What |  channels |  can |  you |  use |  to |  reach |  and |  engage |  with |  your |  target |  audience |  ( | e | .g | . |  social |  media | , |  email |  marketing | , |  online |  advertising | )?
 | 5 | . |  Have |  you |  considered |  forming |  partnerships |  or |  collaborations |  with |  other |  companies |  or |  influencers |  to |  help |  promote |  your |  AI |  services | ?
 | 6 | . |  Are |  there |  any |  industry |  events |  or |  conferences |  where |  you |  can |  showcase |  your |  AI |  services |  and |  connect |  with |  potential |  customers | ?
 | 7 | . |  How |  can |  you |  use |  customer |  testimonials |  and |  case |  studies |  to |  demonstrate |  the |  value |  and |  effectiveness |  of |  your |  AI |  services | ?
 | 8 | . |  Have |  you |  considered |  offering |  free |  trials |  or |  discounts |  to |  incentiv | ize |  potential |  customers |  to |  try |  out |  your |  AI |  services | ?
 | 9 | . |  Are |  there |  any |  niche |  or |  specialized |  online |  communities |  where |  your |  target |  audience |  congreg | ates |  that |  you |  can |  participate |  in |  and |  promote |  your |  AI |  services | ?
 | 10 | . |  What |  metrics |  or |  K | PI | s |  will |  you |  use |  to |  track |  the |  success |  of |  your |  marketing |  efforts |  and |  adjust |  your |  strategy |  accordingly | ? |  | 
"""