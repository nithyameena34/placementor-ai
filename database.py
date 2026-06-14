import sqlite3

# Connect Database
conn = sqlite3.connect("placementor.db", check_same_thread=False)

# Cursor
cursor = conn.cursor()

# Create Chat Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")

conn.commit()

# Save Message
def save_message(role, message):

    cursor.execute(
        "INSERT INTO chat_history (role, message) VALUES (?, ?)",
        (role, message)
    )

    conn.commit()

# Get Chat History
def get_messages():

    cursor.execute(
        "SELECT role, message FROM chat_history"
    )

    return cursor.fetchall()
