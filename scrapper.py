import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"

def scrape_books():
    response = requests.get(BASE_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        image = BASE_URL + book.find("img")["src"].replace("../", "")

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "image": image
        })

    return books