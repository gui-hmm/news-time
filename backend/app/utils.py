from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Configuração do Passlib para hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuração do JWT
SECRET_KEY = "sua_chave_secreta_muito_segura"  # Altere para um segredo forte
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # O token expira em 60 minutos

def hash_password(password: str) -> str:
    """Gera o hash da senha usando bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha fornecida corresponde ao hash armazenado"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Cria um token de acesso JWT"""
    to_encode = data.copy()
    expire = datetime.now(tz=datetime.UTC)() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
