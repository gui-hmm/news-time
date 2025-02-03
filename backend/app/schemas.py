from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Schemas para Usuário
class UserBase(BaseModel):
    username: str
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True

# Schemas para Notícias
class NewsBase(BaseModel):
    article_id: str
    title: str

class NewsCreate(NewsBase):
    pass

class NewsOut(NewsBase):
    likes: int
    favorites: int
    comments: List[str]

    class Config:
        from_attributes = True

# Schemas para Likes
class LikeBase(BaseModel):
    user_id: int
    article_id: str

class LikeCreate(LikeBase):
    pass

class LikeOut(LikeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Schemas para Favoritos
class FavoriteBase(BaseModel):
    user_id: int
    article_id: str

class FavoriteCreate(FavoriteBase):
    pass

class FavoriteOut(FavoriteBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Schemas para Comentários
class CommentBase(BaseModel):
    user_id: int
    article_id: str
    content: str

class CommentCreate(CommentBase):
    pass

class CommentOut(CommentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
