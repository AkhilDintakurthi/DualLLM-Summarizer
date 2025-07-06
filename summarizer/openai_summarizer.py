from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model = "gpt-4o-mini", max_tokens=1000)

prompt = PromptTemplate(
    template="You are a helpful assistant that summarizes text. Please summarize the following text:\n\n{text}\n\nSummary:",
    input_variables=["text"]
)

summarizer = prompt | model

def summarize_with_openai(scraped_data: dict) -> str:
    title = scraped_data.get("title", "No Title")
    text = scraped_data.get("text", "No Content")

    if not text.strip():
        return f"{title}\nNo content to summarize."
    
    try:
        response = summarizer.invoke({"text": text})
        summary = response.content.strip()
    except Exception as e:
        summary = f"Error summarizing text: {str(e)}"

    return f"{title}\n\nSummary:\n{summary}"

if __name__ == "__main__":
    from scraper.web_scraper import get_page_content

    url = "https://techcrunch.com/2025/07/03/wonder-dynamics-co-founder-nikola-todorovic-joins-the-ai-stage-at-techcrunch-disrupt-2025/"
    scraped_data = get_page_content(url)

    summary = summarize_with_openai(scraped_data)
    print(summary)


