
from fastapi import APIRouter, Depends, status, Response
#from fastapi import Depends, FastAPI, HTTPException, Response, status,APIRouter
from typing import List
from sqlalchemy.orm import Session
from blog import schemas, database, models
from blog.hashing import Hash


# Users


def create(user: schemas.User, db:Session):
	new_user = models.User(name = user.name,
							email = user.email,
							password = Hash.bcrypt(user.password))
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user

def show(id,response: Response, db:Session):
	user = db.query(models.User).filter(models.User.id == id).first()
	if not user:
		response.status_code = status.HTTP_404_NOT_FOUND
		return {'default':f'User with the id {id} is not available' }
	return user
