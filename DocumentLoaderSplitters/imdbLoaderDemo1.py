from langchain_community.document_loaders import IMSDbLoader

loader = IMSDbLoader("https://www.imdb.com/scripts/BlacKkKlansman.html")
imdbdata =loader.load()
format_text= imdbdata[0].page_content[:5000].strip()
print(format_text)