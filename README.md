# 📊 Data Analytics Internship Projects

## 📌 About the Project
This repository contains Python-based data analytics tasks completed as part of my Data Analytics Internship. The projects cover web scraping, data cleaning, exploratory data analysis (EDA), and data visualization using Python libraries.

## 🎯 Objectives
- Collect book data from a website using web scraping.
- Clean and analyze the collected dataset.
- Explore book prices and ratings.
- Create visualizations to understand the data.

## 🛠️ Technologies Used
- Python
- Pandas
- Requests
- BeautifulSoup
- Matplotlib
- VS Code

## 📂 Project Structure

```text
Data-Analytics/
│
├── web_scraping.py
├── eda_analysis.py
├── visualization.py
├── books_dataset.csv
├── price_distribution.png
├── rating_distribution.png
└── top_10_expensive_books.png
```

## 🚀 Tasks Completed

### Task 1: Web Scraping
- Scraped book details from [Books to Scrape](https://books.toscrape.com/).
- Extracted book titles, prices, and ratings.
- Stored the collected data in a CSV file using Pandas.

**File:** `web_scraping.py`

### Task 2: Exploratory Data Analysis (EDA)
- Loaded and explored the dataset.
- Checked dataset shape, column names, and data types.
- Cleaned the Price column by removing currency symbols.
- Checked for missing values.
- Calculated average, maximum, and minimum book prices.
- Analyzed the distribution of book ratings.

**File:** `eda_analysis.py`

### Task 3: Data Visualization
Created visualizations to understand the dataset:
- Book Price Distribution — histogram of book prices.
- Rating Distribution — bar chart of book ratings.
- Top 10 Most Expensive Books — horizontal bar chart.

**File:** `visualization.py`

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install pandas requests beautifulsoup4 matplotlib
```

## ▶️ How to Run

**Step 1:** Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2:** Open the project folder in VS Code.

**Step 3:** Run the scripts in the following order:

```bash
python web_scraping.py
python eda_analysis.py
python visualization.py
```

The first script generates `books_dataset.csv`. The visualization script generates three chart images.

## 📈 Key Learnings
- Understanding web scraping with Requests and BeautifulSoup.
- Data cleaning and preprocessing using Pandas.
- Performing exploratory data analysis.
- Creating charts using Matplotlib.
- Working with CSV datasets in Python.

## 👩‍💻 Author
**Parkavi P**

Data Analytics Intern | MCA Student

---

⭐ Thank you for visiting my repository!
