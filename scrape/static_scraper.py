import requests
from bs4 import BeautifulSoup

def scrape_chapter(url: str) -> str:
    print(f"🧭 Fetching chapter from: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_div = soup.find('div', {'id': 'mw-content-text'})
    if not content_div:
        raise ValueError("❌ Could not find #mw-content-text.")

    paragraphs = content_div.find_all(['p', 'h2', 'h3'])
    chapter_text = "\n\n".join(p.get_text(strip=True) for p in paragraphs)

    print("✅ Chapter successfully scraped.")
    return chapter_text
