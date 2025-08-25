import os
import sqlite3

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

conn = sqlite3.connect("./data/main.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS expenses (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       amount INTEGER NOT NULL,
       category TEXT NOT NULL
    )
"""
)

categories = [
    "housing",
    "transportation",
    "food",
    "utilities",
    "clothing",
    "healthcare",
    "insurance",
    "supplies",
    "personal",
    "debt",
    "retirement",
    "education",
    "savings",
    "gifts",
    "entertainment",
]


class Record(BaseModel):
    id: int | None = None
    amount: int
    category: str


def insert_record(amount: int, category: str):
    cursor.execute(
        "INSERT INTO expenses (amount, category) VALUES (?, ?)",
        (amount, category),
    )
    conn.commit()
    return cursor.lastrowid


def get_records():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    records = []
    for row in rows:
        record = {}
        record["id"] = row[0]
        record["amount"] = row[1]
        record["category"] = row[2]
        records.append(record)
    return records


def delete_item(item_id: int):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (str(item_id)))
    conn.commit()


def get_category_total(category: str):
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (str(category),))
    rows = cursor.fetchall()
    total = 0
    for row in rows:
        total += row[1]
    return total


def get_from_category(category: str):
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (str(category),))
    rows = cursor.fetchall()
    records = []
    for row in rows:
        record = {}
        record["id"] = row[0]
        record["amount"] = row[1]
        record["category"] = row[2]
        records.append(record)
    return records


def get_total():
    total = {"total": 0}
    for c in categories:
        num = get_category_total(c)
        total["total"] += num
        total[c] = num

    return total
