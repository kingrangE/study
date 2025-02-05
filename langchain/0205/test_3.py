from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

"""
prompt, llm chain 연결 후 invoke 해봅니다.
"""
llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template("You're an expert in DevOps. So you're good at answering how to deploy app using AWS service. now please answer this question. Question : {question}")

chain = prompt|llm

output = chain.invoke({"question": "how to deploy a web application with AWS? My web application is consist of Flask, static web files and MySQL"})
print(output)

"""
출력 결과 : 
content="To deploy a web application with Flask, static web files, and MySQL on AWS, you can follow these general steps:\n\n1. Set up an Amazon EC2 instance:\n   
- Launch an EC2 instance running your preferred operating system (e.g. Amazon Linux, Ubuntu).\n   
- Set up security groups to allow inbound traffic on ports 80 (HTTP), 443 (HTTPS), and 22 (SSH).\n   
- Connect to your EC2 instance using SSH.\n\n2. Install necessary software:\n   - Install Python and Flask on your EC2 instance.\n   
- Install MySQL server on your EC2 instance.\n   - Set up a MySQL database for your web application.\n\n3. Configure and deploy your Flask application:\n   
- Copy your Flask application files to the EC2 instance.\n   
- Modify the Flask application to connect to the MySQL database.\n   
- Install any necessary Python packages using pip.\n   
- Run the Flask application using a WSGI server like Gunicorn or uWSGI.\n\n
4. Configure and serve static web files:\n   
- Set up an Amazon S3 bucket to store your static web files.\n   
- Upload your static web files to the S3 bucket.\n   
- Configure Amazon CloudFront to serve the static web files from the S3 bucket.\n\n
5. Set up a domain name and SSL certificate:\n   
- Register a domain name using Route 53 or a third-party domain registrar.\n   
- Obtain an SSL certificate from AWS Certificate Manager or a third-party certificate authority.\n   
- Configure the SSL certificate for your domain in the load balancer or web server configuration.\n\n
6. Configure a load balancer (optional):\n   
- Set up an Elastic Load Balancer to distribute incoming traffic to your EC2 instances.\n   
- Configure the load balancer to forward traffic to the EC2 instance serving your Flask application.\n\n
7. Test and monitor your deployment:\n   
- Access your web application using the domain name and verify that it is working correctly.\n   
- Set up monitoring and logging using Amazon CloudWatch to keep track of your application's performance and health.\n\n
These are high-level steps to deploy a web application with Flask, static web files, and MySQL on AWS. The exact steps and tools used may vary depending on your specific requirements and architecture. 
It's recommended to refer to the AWS documentation and best practices for more detailed guidance." 
additional_kwargs={'refusal': None} 
response_metadata={'token_usage': {'completion_tokens': 473, 'prompt_tokens': 59, 'total_tokens': 532, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 
'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-0dc5a83e-4fa2-47e8-9510-955b3ed3f8e9-0' 
usage_metadata={'input_tokens': 59, 'output_tokens': 473, 'total_tokens': 532, 'input_token_details': {'audio': 0, 'cache_read': 0}, 
'output_token_details': {'audio': 0, 'reasoning': 0}}

ps. This paragraph has been split by me.
"""