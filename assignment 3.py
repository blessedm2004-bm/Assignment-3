import os
import random
import re
import socket
import sqlite3
import urllib.request
import json

# --------------------------
# Q1. Classify integer
# --------------------------
def classify_integer():
    try:
        n = int(input("Enter an integer: "))
        if n > 0:
            print("Positive")
        elif n < 0:
            print("Negative")
        else:
            print("Zero")
    except ValueError:
        print("Invalid input, please enter an integer.")

# --------------------------
# Q2. Average of numbers (*args)
# --------------------------
def average_numbers(*nums):
    if nums:
        return sum(nums) / len(nums)
    return 0

# --------------------------
# Q3. File handling (write & read)
# --------------------------
def file_handling():
    with open("sample.txt", "w") as f:
        f.write("Hello, this is a test file.\nPython makes it easy!")
    with open("sample.txt", "r") as f:
        content = f.read()
    print("File content:\n", content)

# --------------------------
# Q4. Celsius → Fahrenheit using map + lambda
# --------------------------
def convert_temperatures():
    celsius = [0, 10, 20, 30, 40]
    fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))
    print("Celsius:", celsius)
    print("Fahrenheit:", fahrenheit)

# --------------------------
# Q5. Division with exception handling
# --------------------------
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

# --------------------------
# Q6. Custom exception for negative numbers
# --------------------------
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers not allowed")
    print(f"{n} is valid!")

# --------------------------
# Q7. Random numbers & average
# --------------------------
def random_average():
    nums = [random.randint(1, 100) for _ in range(10)]
    print("Numbers:", nums)
    print("Average:", sum(nums) / len(nums))

# --------------------------
# Q8. Regex examples
# --------------------------
def regex_examples():
    text = "Emails: test@example.com, hello@mail.com"
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
    print("Extracted emails:", emails)

    date = "2025-09-13"
    if re.match(r"\d{4}-\d{2}-\d{2}", date):
        print("Valid date format")

    replaced = re.sub(r"Python", "Java", "I love Python programming")
    print("After replace:", replaced)

    words = re.split(r"\s+", "Split this sentence")
    print("Split words:", words)

# --------------------------
# Q9. Simple client-server (demo)
# --------------------------
def simple_server():
    # Run this in one script (server)
    s = socket.socket()
    s.bind(("localhost", 9999))
    s.listen(1)
    print("Server listening...")
    conn, addr = s.accept()
    print("Connected:", addr)
    conn.send(b"Hello from server")
    conn.close()

def simple_client():
    # Run this separately (client)
    s = socket.socket()
    s.connect(("localhost", 9999))
    data = s.recv(1024)
    print("Received:", data.decode())
    s.close()

# --------------------------
# Q10. SQLite basic example
# --------------------------
def sqlite_example():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users VALUES (?, ?)", (1, "Blessed"))
    conn.commit()
    for row in cursor.execute("SELECT * FROM users"):
        print(row)
    conn.close()

# --------------------------
# Q11. API request + SQLite (urllib)
# --------------------------
def fetch_and_store():
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")

        json_data = json.loads(data)
        print("Fetched from API:", json_data)

        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER, title TEXT, body TEXT)")
        cursor.execute("INSERT INTO posts (id, title, body) VALUES (?, ?, ?)",
                       (json_data["id"], json_data["title"], json_data["body"]))
        conn.commit()
        conn.close()
        print("Data stored in database successfully!")

    except Exception as e:
        print("Error:", e)

# --------------------------
# MAIN (demo run)
# --------------------------
if __name__ == "__main__":
    # You can uncomment the functions to test them
    # classify_integer()
    print("Average of 2, 4, 6:", average_numbers(2, 4, 6))
    file_handling()
    convert_temperatures()
    print("Safe division 10/2:", safe_division(10, 2))
    print("Safe division 10/0:", safe_division(10, 0))
    try:
        check_positive(5)
        check_positive(-3)
    except NegativeNumberError as e:
        print("Caught error:", e)
    random_average()
    regex_examples()
    sqlite_example()
    fetch_and_store()

