from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import Article
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/articles")
def get_articles(db:Session = Depends(get_db)):
    articles = db.query(Article).all()
    return articles

@app.get("/articles/{article_id}")
def get_article(article_id:int, db:Session = Depends(get_db)):
    article_model = db.query(Article).filter(Article.id == article_id).first()

    if article_model is None:
        raise HTTPException(
            status_code=404,
            detail="This article does not exist"
        )

    return article_model

@app.delete("/articles/{article_id}")
def get_article(article_id:int, db:Session = Depends(get_db)):
    article_model = db.query(Article).filter(Article.id == article_id).first()

    if article_model is None:
        raise HTTPException(
            status_code=404,
            detail="This article does not exist"
        )
    db.query(Article).filter(Article.id == article_id).delete()
    db.commit() 

    return {"Success":"Article deleted"}