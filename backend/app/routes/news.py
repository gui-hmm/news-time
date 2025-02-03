from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/news", tags=["news"])

@router.get("/{article_id}", response_model=schemas.NewsOut)
def get_news(article_id: str, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.article_id == article_id).first()
    if not news:
        return {"message": "Notícia não encontrada"}
    return news
