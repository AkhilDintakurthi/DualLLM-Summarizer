# scraper/web_scraper.py

from scraper.scraper import scrape_title_and_article

def get_page_content(url: str) -> dict:
    title, text = scrape_title_and_article(url)

    return {
        "title": title,
        "text": text,
        "source": url
    }


if __name__ == "__main__":
    url = "https://example.com/your-article-here"
    result = get_page_content(url)
    
    print(f"Title: {result['title']}\n")
    print(f"Content Preview:\n{result['text'][:1000]}")  # Limit output for readability
    print(f"\nSource URL: {result['source']}")