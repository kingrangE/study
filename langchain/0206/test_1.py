"""RAG의 전 과정을 간단하게 실습합니다.
1. document loader
2. text splitter
3. indexing

"""
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
#이동욱 개발자님의 블로그 글을 가져옵니다.
url = "https://jojoldu.tistory.com/816"
urls = ["https://wikidocs.net/231393","https://wikidocs.net/231364"]
loader = WebBaseLoader(urls) #web_path: Union[str, Sequence[str]] = "", (url 1개도 되고 여러 개도 가능합니다.)

# loader객체에 있는 url을 Documents로 변환하여 docs 변수에 저장합니다.
docs = loader.load() 

print(docs) # Document객체가 들어있는 리스트가 반환됩니다. (def load(self) -> list[Document]:)
print(len(docs)) # 리스트의 길이를 반환합니다. (url의 개수와 같습니다.)
print(len(docs[0].page_content)) # 리스트 첫 Document의 page 내용의 길이를 확인합니다.
print(docs[0].page_content[1000:2000]) # 첫 Document의 1000~2000번째 text를 출력합니다.


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
splits = text_splitter.split_documents(docs)

print(len(splits))
print(splits[3:4])
print(splits[0].page_content)
print(splits[0].metadata)

vector_store = Chroma.from_documents(splits,embedding=OpenAIEmbeddings()) # docs를 OpenAIEmbedding으로 임베딩하여 vector_store로 만듦
docs = vector_store.similarity_search("Indexing은 어떻게 하나요??") # 질문을 하면 가장 유사한 페이지를 찾음
print(len(docs))
print(docs[0].page_content)