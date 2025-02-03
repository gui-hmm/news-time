from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/")
def add_comment(comment: schemas.CommentBase, db: Session = Depends(get_db)):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    return {"message": "Comentário adicionado"}
