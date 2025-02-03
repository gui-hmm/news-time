from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/")
def favorite_news(fav: schemas.FavoriteBase, db: Session = Depends(get_db)):
    db_fav = models.Favorite(**fav.dict())
    db.add(db_fav)
    db.commit()
    return {"message": "Favorito adicionado"}
