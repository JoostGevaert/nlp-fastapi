from typing import List

from fastapi import FastAPI
from ml import nlp
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "Hello World"}

class Article(BaseModel):
    content: str
    comments: List[str] = []

@app.post("/article/")
def analyze_article(article: Article):
    return {"message": article.content, "comments": article.comments}


