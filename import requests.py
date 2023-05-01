import requests
from bs4 import BeautifulSoup
import sqlite3

# Step 1: Send a GET request to the website
response = requests.get("http://quotes.toscrape.com/")
#print('response:',response)
# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
#print('SOUP:',soup)
# Step 3: Find all the quotes on the page
quotes = soup.find_all("div", {"class": "quote"})
print('QUOTES:',quotes)
# Step 4: Connect to the SQLite database
conn = sqlite3.connect("quotes.db")

# Step 5: Create a new table to store the quotes
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS quotes (
        author TEXT NOT NULL,
        text TEXT NOT NULL
    );
    """
)

# Step 6: Insert the quotes into the database
for quote in quotes:
    author = quote.find("small", {"class": "author"}).get_text()
    text = quote.find("span", {"class": "text"}).get_text()
    print(author, text)
    conn.execute(
        """
        INSERT INTO quotes (author, text)
        VALUES (?, ?);
        """,
        (author, text)
    )
conn.commit()

# Step 7: Close the database connection
conn.close()
