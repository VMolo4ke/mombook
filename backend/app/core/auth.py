import os
import datetime
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ADMIN_USER = os.getenv("ADMIN_USERNAME")
ADMIN_PASS = os.getenv("ADMIN_PASSWORD")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login/") # URL где получаем токен

def create_access_token(username: str):
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    return jwt.encode({"sub": username, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)

# Зависимость для защиты роутеров
def verify_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username != ADMIN_USER:
            raise HTTPException(status_code=403, detail="Not authorized")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")