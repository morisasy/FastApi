
#from fastapi import APIRouter, Depends, status, Response
from fastapi import Depends, FastAPI, HTTPException, Response, status,APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..crud import blog



router = APIRouter(
    prefix="/login",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post('/')
def login(request:schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail = f'Invalid credentials')

    return user
