import sqlite3
import uuid

# Connect to in-memory DB (use a file for persistence)
conn = sqlite3.connect("db.sqlite")  # or "example.db"
cursor = conn.cursor()

# Step 1: Create user table
cursor.execute("""
CREATE TABLE user (
    email TEXT PRIMARY KEY,
    name TEXT NOT NULL
)
""")

# Step 2: Create token table
cursor.execute("""
CREATE TABLE token (
    token TEXT PRIMARY KEY,
    email TEXT NOT NULL,
    FOREIGN KEY(email) REFERENCES user(email),
    UNIQUE(token, email)
)
""")

# Step 3: Insert data

# Sample users
users = list()
for i, user in enumerate(['alice', 'bob', 'rahul', 'rohan', 'priya', 'sakshi', 'aman',' aditya', 'arpita', 'roshini', 'dan', 'damini']):
    for j in range(100):
        users.append(
        (f'{i}{user}{j}@example.com', f'{user[0].upper()}{user[1:]}{i}{j}')
    )

print(len(users))
# Insert users
cursor.executemany("INSERT INTO user (email, name) VALUES (?, ?)", users)

# Generate tokens
tokens = [(str(uuid.uuid4()), i[0]) for i in users]
print(tokens[0])
# Insert tokens
cursor.executemany("INSERT INTO token (token, email) VALUES (?, ?)", tokens)

# Verify
# for row in cursor.execute("SELECT * FROM user"):
#     print("User:", row)
#
# for row in cursor.execute("SELECT * FROM token"):
#     print("Token:", row)

# Commit if needed and close
conn.commit()
conn.close()
