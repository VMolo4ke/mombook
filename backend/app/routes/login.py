from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# Импортируйте только то, что НЕ импортирует этот роутер обратно
from app.core.auth import ADMIN_PASS, ADMIN_USER, create_access_token 

router = APIRouter(prefix="/api/login", tags=["Login"])

@router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Логика проверки
    if form_data.username == ADMIN_USER and form_data.password == ADMIN_PASS:
        token = create_access_token(form_data.username)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")