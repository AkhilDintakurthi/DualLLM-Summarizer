# scraper/scraper.py

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def scrape_title_and_article(url: str) -> tuple[str, str]:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            logging.info(f"Navigating to {url}")
            page.goto(url, timeout=60000)
            page.wait_for_selector("body")
            html = page.content()
            browser.close()

        # Parse the rendered HTML with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "aside", "form", "header", "noscript", "img", "svg"]):
            tag.decompose()
        for tag in soup.select(".advertisement, .share-buttons, .related-articles, .comments, .newsletter"):
            tag.decompose()
        
        title = soup.title.string.strip() if soup.title else ""

        # Try to get the main content area (fallback to <body> if nothing found)
        #article = soup.find("article") or soup.find("main") or soup.body
        text = soup.get_text(separator="\n", strip=True) #if article else ""

        return title, text

    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return "", ""

# Optional standalone test
if __name__ == "__main__":
    url = "https://example.com/your-article-here"
    title, text = scrape_title_and_article(url)
    print(f"Title:\n{title}\n")
    print(f"Content Preview:\n{text}")
