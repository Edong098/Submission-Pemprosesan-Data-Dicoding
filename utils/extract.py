import requests # type: ignore
import time
from bs4 import BeautifulSoup # type: ignore
from datetime import datetime

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/96.0.4664.110 Safari/537.36"
    )
}

def fetching_content(url):
    """Mengambil konten HTML dari URL."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None


from datetime import datetime
import re

def extract_product_data(card):
    """Mengambil data produk dari satu card."""
    try:
        title = card.find("h3", class_="product-title").text.strip()

        price_tag = card.find("span", class_="price")
        price = price_tag.text.strip() if price_tag else None

        info = card.find_all("p", style=True)

        raw_rating = info[0].text if len(info) > 0 else ""
        match_rating = re.search(r"(\d+\.?\d*)", raw_rating)
        rating = float(match_rating.group(1)) if match_rating else 0.0

        colors = info[1].text.replace("Colors", "").strip() if len(info) > 1 else None
        size = info[2].text.replace("Size:", "").strip() if len(info) > 2 else None
        gender = info[3].text.replace("Gender:", "").strip() if len(info) > 3 else None

        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": datetime.now()
        }

    except Exception as e:
        print(f"Error parsing product: {e}")
        return None

def scrape_main(base_url, start_page=1, end_page=50, delay=1):
    """Fungsi utama scraping (Extract)."""
    products = []

    try:
        for page in range(start_page, end_page + 1):
            if page == 1:
                url = base_url
            else:
                url = f"{base_url}page{page}"

            print(f"Scraping halaman {page} → {url}")

            html = fetching_content(url)
            if not html:
                continue

            soup = BeautifulSoup(html, "html.parser")
            cards = soup.find_all("div", class_="collection-card")

            for card in cards:
                product = extract_product_data(card)
                if product:
                    products.append(product)

            time.sleep(delay)

        print(f"Total data berhasil diambil: {len(products)}")
        return products

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return []
