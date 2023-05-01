import sqlite3

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("quotes.db")

# Step 2: Query the database to get all the quotes
cursor = conn.execute("SELECT author, text FROM quotes")
quotes = cursor.fetchall()

# Step 3: Print the quotes
for author, text in quotes:
    print(f"{author}: {text}\n")
    
# Step 4: Close the database connection
conn.close()
