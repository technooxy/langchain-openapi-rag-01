import requests
from bs4 import BeautifulSoup

# List of Amazon product URLs
product_urls = [
    "https://www.amazon.in/dp/B08L5VZKWT",
    "https://www.amazon.in/dp/B07VJYZF24",
    # Add more URLs here
]

for url in product_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
    # # Extract product details (similar to previous example)
    # product_title = soup.find("span", {"id": "productTitle"}).get_text().strip()
    # product_price = soup.find("span", {"id": "priceblock_ourprice"}).get_text().strip()

    # # Print or store the extracted information
    # print(f"Product Title: {product_title}")
    # print(f"Product Price: {product_price}")
    # print("-" * 30)  # Separator between products
