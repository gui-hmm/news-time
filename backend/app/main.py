from fastapi import FastAPI
from .database import engine, Base
from .routes import user, news, likes, favorites, comments

app = FastAPI()

# Incluir rotas
app.include_router(user.router)
app.include_router(news.router)
app.include_router(likes.router)
app.include_router(favorites.router)
app.include_router(comments.router)

@app.get("/")
def root():
    return {"message": "API de Notícias Rodando 🚀"}
