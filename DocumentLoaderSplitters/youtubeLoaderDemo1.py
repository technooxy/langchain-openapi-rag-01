from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=ymyDyusbcHI", 
    add_video_info=False,
    language=["en","id"],
    translation="en"
    )
youtubedata =loader.load()
format_text= youtubedata[0].page_content[:5000].strip()
print(format_text)