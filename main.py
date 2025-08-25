import json

import requests
from fastapi import FastAPI

app = FastAPI()

import db


@app.get("/")
def get_records():
    return db.get_records()


@app.post("/")
def create_record(body: str):
    response = requests.post(
        "http://ollama:11434/api/generate",
        json={
            "model": "geld-llama3",
            "prompt": body,
            "stream": False,
        },
    ).json()
    response = json.loads(response["response"])
    rowid = db.insert_record(response["spent"], response["category"].lower())
    record = {
        "id": rowid,
        "amount": response["spent"],
        "category": response["category"].lower(),
    }
    return record


@app.get("/total")
def get_total():
    return db.get_total()


@app.delete("/{item_id}")
def delete_item(item_id: int):
    db.delete_item(item_id)
    return "success"


@app.get("/{category}")
def get_spent_on_category(category: str):
    return {
        "category": category,
        "spent": db.get_category_total(category),
        "records": db.get_from_category(category),
    }
