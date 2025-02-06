"""RAG의 전 과정을 간단하게 실습합니다."""
from langchain_community.document_loaders import WebBaseLoader

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