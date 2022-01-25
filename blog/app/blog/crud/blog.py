
from fastapi import APIRouter, Depends, status, Response
#from fastapi import Depends, FastAPI, HTTPException, Response, status,APIRouter
from typing import List
from sqlalchemy.orm import Session
from blog import schemas, database, models
#rom ...crud import blog



#from . import models, schemas

 # Blogs
def get_all(db:Session):
	blogs = db.query(models.Blog).all()
	return blogs

def create(blog: schemas.Blog, db:Session):
	new_blog = models.Blog(title = blog.title,
                            body = blog.body,
                            user_id=1)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)
	return new_blog

def delete(id, db:Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id)
	if not blog.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail = f'Blog with id {id} not found')
	blog.delete(synchronize_session=False)
	db.commit()
	return blog

def update(id, request: schemas.Blog, db:Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id)
	if not blog.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail = f'Blog with id {id} not found')
	blog.update(request)
	blog.commit()
	return blog


def show(id, db:Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id)
	if not blog.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
		                    detail = f'Blog with id {id} not found')
	return blog
