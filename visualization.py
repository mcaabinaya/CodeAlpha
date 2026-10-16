import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Clean Price column
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.strip()
    .astype(float)
)

# Chart 1: Price Distribution
plt.figure()
plt.hist(df["Price"], bins=5)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.savefig("price_distribution.png")
plt.show()


# Chart 2: Rating Distribution
plt.figure()
df["Rating"].value_counts().plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.savefig("rating_distribution.png")
plt.show()


# Chart 3: Top 10 Expensive Books
top_books = df.sort_values("Price", ascending=False).head(10)

plt.figure()
plt.barh(top_books["Title"], top_books["Price"])

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")

plt.tight_layout()

plt.savefig("top_10_expensive_books.png")
plt.show()

print("All charts created successfully!")