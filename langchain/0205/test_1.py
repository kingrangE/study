from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

"""
OPENAI를 이용한 질문 및 응답 받기
"""
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

output = llm.invoke("How to deploy a web application using AWS services")
print(output)

"""
출력 결과 : 
content="Deploying a web application on AWS involves selecting the appropriate services and configuring them to host your application. 
Here's a general outline of the steps involved in deploying a web application using AWS services:\n\n
1. Develop and test your web application: Before deploying your application, make sure it is fully developed and tested to ensure it functions as expected.\n\n
2. Choose a hosting option: AWS offers several hosting options for web applications, including Elastic Beanstalk, EC2, and S3. Choose the option that best fits your application's requirements.\n\n
3. Set up an AWS account: If you don't already have an AWS account, sign up for one at aws.amazon.com and create an account.\n\n
4. Configure your AWS resources: Depending on the hosting option you choose, you'll need to configure your AWS resources accordingly. For example, if you choose Elastic Beanstalk, you'll need to create an application and environment. 
If you choose EC2, you'll need to launch an instance and set up a security group.\n\n5. Upload your application files: Once your resources are configured, upload your application files to your AWS resources. 
This may involve using the AWS Management Console, the AWS CLI, or another tool.\n\n6. Test your application: After uploading your application files, test your application to ensure it is functioning correctly on AWS.\n\n
7. Set up a domain name: If you want to use a custom domain name for your web application, you'll need to set up a domain name using Route 53 or another domain registrar.\n\n
8. Configure security settings: Make sure to configure security settings for your application to protect it from unauthorized access.\n\n
9. Monitor and scale your application: Once your application is deployed, monitor its performance and scale it as needed to accommodate increased traffic.\n\n
10. Backup and maintain your application: Regularly backup and maintain your application to ensure it continues to run smoothly on AWS.\n\n
By following these steps, you can successfully deploy your web application using AWS services." 
additional_kwargs={'refusal': None} 
response_metadata={'token_usage': {'completion_tokens': 396, 'prompt_tokens': 16, 'total_tokens': 412, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-a33b34ad-ae7c-4c91-a5b8-6c3b90360142-0' 
usage_metadata={'input_tokens': 16, 'output_tokens': 396, 'total_tokens': 412, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

ps. This paragraph has been split by me.
"""