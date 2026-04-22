from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("КРИТИЧЕСКАЯ ОШИБКА: Переменная окружения DATABASE_URL не задана!")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SnippetDB(Base):
    __tablename__ = "snippets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    command = Column(String)
    description = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DevOps Snippet Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Snippet(BaseModel):
    title: str
    command: str
    description: str = "Нет описания"

@app.get("/")
def read_root():
    return {"message": "API подключено к базе PostgreSQL!"}

@app.get("/snippets")
def get_snippets():
    db = SessionLocal()
    snippets = db.query(SnippetDB).all()
    db.close()
    return snippets

@app.post("/snippets")
def add_snippet(snippet: Snippet):
    db = SessionLocal()
    new_snippet = SnippetDB(title=snippet.title, command=snippet.command, description=snippet.description)
    db.add(new_snippet)
    db.commit()
    db.close()
    return {"status": "Успешно сохранено в Postgres", "snippet": snippet.title}