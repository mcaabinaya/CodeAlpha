import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Get webpage
response = requests.get(url)

# Convert HTML into BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Empty list to store data
books = []

# Find all books
for book in soup.select(".product_pod"):

    # Get book title
    title = book.h3.a["title"]

    # Get price
    price = book.select_one(".price_color").text

    # Get rating
    rating = book.p["class"][1]

    # Store data
    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

# Convert to DataFrame
df = pd.DataFrame(books)

# Display data
print(df)

# Save as CSV
df.to_csv("books_dataset.csv", index=False)

print("\nDataset created successfully!")