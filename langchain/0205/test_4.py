from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

"""output parser까지 체인에 연결하여 결과값의 텍스트만 가져옵니다."""

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template("You're an expert in DevOps. So you're good at answering how to deploy app using AWS service. now please answer this question. Question : {question}")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

output = chain.invoke({"question": "how to deploy a web application with AWS? My web application is consist of Flask, static web files and MySQL"})

print(output)

""" 
To deploy a web application with AWS that consists of Flask, static web files, and MySQL, you can follow these steps:

1. Set up your Flask application: Make sure your Flask application is set up and running locally. Test it to ensure it is working as expected.

2. Create an RDS instance for MySQL: Use the AWS Management Console to create a new RDS database instance for MySQL. Make sure to note down the endpoint, username, and password for the database.

3. Upload static web files to an S3 bucket: Create an S3 bucket on AWS and upload your static web files (HTML, CSS, JavaScript, images, etc.) to the bucket.

4. Configure your Flask application: Update your Flask application to connect to the RDS MySQL database. You can use SQLAlchemy or any other ORM library to handle database connections.

5. Create an EC2 instance: Launch an EC2 instance on AWS where you will deploy your Flask application. Make sure to install all the necessary dependencies for your application.

6. Secure your EC2 instance: Set up security groups to control inbound and outbound traffic to your EC2 instance. You may also want to configure IAM roles and instance profiles for additional security.

7. Deploy your Flask application: Copy your Flask application files to the EC2 instance using SSH or an SFTP client. Install any necessary libraries and dependencies on the EC2 instance.

8. Configure your web server: Set up a web server like Nginx or Apache on the EC2 instance to serve static files and proxy requests to your Flask application.

9. Update DNS records: Update your DNS settings to point to the public IP address of your EC2 instance so that users can access your web application.

10. Test the deployment: Access your web application using the domain name or IP address of your EC2 instance to ensure that everything is working correctly.

By following these steps, you should be able to successfully deploy your Flask web application with static web files and MySQL on AWS. Let me know if you need more detailed guidance on any of these steps.

ps. This paragrah have been split by itself
"""