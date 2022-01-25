# blog/app/routers
from fastapi import APIRouter, Depends, status, Response
#from fastapi import Depends, FastAPI, HTTPException, Response, status,APIRouter
from typing import List
from sqlalchemy.orm import Session
from blog import schemas, database, models
from blog.hashing import Hash
from blog.crud import user

router = APIRouter(
		prefix="/user",
		tags=["Users"]
)

get_db =database.get_db


@router.post('/', response_model = schemas.ShowUser)
def create(request: schemas.User, db:Session=Depends(get_db)):
	return user.create(request, db)

@router.get('/{id}', status_code=200, response_model = schemas.ShowUser)
def show(id,response: Response, db:Session=Depends(get_db)):
	return user.show(id, response, db)
