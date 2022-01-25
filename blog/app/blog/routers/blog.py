# blog/app/routers

#from fastapi import APIRouter, Depends, status, Response
from fastapi import Depends, FastAPI, HTTPException, Response, status,APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session
from blog import schemas, database, models, oauth2
from blog.crud import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
    responses={404: {"description": "Not found"}},
)

get_db =database.get_db
#blog = crud.blog

@router.get('/', response_model = List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),
    get_current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session=Depends(get_db),
    get_current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.create(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def remove(id, db:Session=Depends(get_db),
    get_current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.delete(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db),
    get_current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.update(id,request, db)


@router.get('/{id}', status_code=200, response_model = schemas.ShowBlog)
def show(id, db:Session=Depends(get_db),
    get_current_user:schemas.User = Depends(oauth2.get_current_user)):
	return blog.show(id, db)
