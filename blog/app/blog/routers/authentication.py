
#from fastapi import APIRouter, Depends, status, Response
from fastapi import Depends, FastAPI, HTTPException, Response, status,APIRouter
from typing import List
from sqlalchemy.orm import Session
from blog import schemas, database, models, token
from blog.hashing import Hash
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

get_db =database.get_db


@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail = f'Invalid credentials')

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail = f'Incorrect password')
    # generate a jwt token and return
    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    """
    return user
    """
