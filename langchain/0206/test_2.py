"""다양한 Document Loader를 실습합니다."""

# 1. Web Base Loader
import bs4
from langchain_community.document_loaders import WebBaseLoader
urls = ['https://tired-o.github.io/posts/github-blog-1/','https://blog.twitch.tv/en/2021/07/16/ubisofts-immortals-fenyx-rising-extension-creators-see-more-hours-watched-and-engagement/']

loader = WebBaseLoader(urls,bs_kwargs=dict(
    parse_only = bs4.SoupStrainer(
        class_ = ("prompt-info") # 지정한 class를 가진 요소만 선택하여 파싱하도록 합니다.
    )
))

docs = loader.load()
print(len(docs))
print(docs)

# 2. Text Loader
from langchain_community.document_loaders import TextLoader

loader = TextLoader('history.txt')
data = loader.load()
print(type(data))
print(len(data))
print(data)
print(data[0].metadata)