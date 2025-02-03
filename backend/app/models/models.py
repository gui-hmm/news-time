from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    likes = relationship("Like", back_populates="user", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")

class News(Base):
    __tablename__ = "news"
    
    article_id = Column(String, primary_key=True)
    title = Column(String, nullable=False)

    likes = relationship("Like", back_populates="news", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="news", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="news", cascade="all, delete-orphan")

class Like(Base):
    __tablename__ = "likes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    article_id = Column(String, ForeignKey("news.article_id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())

    user = relationship("User", back_populates="likes")
    news = relationship("News", back_populates="likes")

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    article_id = Column(String, ForeignKey("news.article_id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())

    user = relationship("User", back_populates="favorites")
    news = relationship("News", back_populates="favorites")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    article_id = Column(String, ForeignKey("news.article_id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())

    user = relationship("User", back_populates="comments")
    news = relationship("News", back_populates="comments")