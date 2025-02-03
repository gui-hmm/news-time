from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/likes", tags=["likes"])

@router.post("/")
def like_news(like: schemas.LikeBase, db: Session = Depends(get_db)):
    db_like = models.Like(**like.dict())
    db.add(db_like)
    db.commit()
    return {"message": "Curtida registrada"}
