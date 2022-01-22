
from fastapi import APIRouter, Depends, status, Response
#from fastapi import Depends, FastAPI, HTTPException, Response, status,APIRouter
from typing import List
from sqlalchemy.orm import Session
from . import schemas, database, models

#from . import models, schemas

 # Blogs
def get_all_blog(db:Session):
	blogs = db.query(models.Blog).all()
	return blogs

def create_blog(blog: schemas.Blog, db:Session):
	new_blog = models.Blog(title = blog.title,
                            body = blog.body,
                            user_id=1)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)
	return new_blog

def delete_blog(id, db:Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id)
	blog.delete(synchronize_session=False)
	db.commit()
	return blog

def update_blog(id, db:Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id)
	blog.update(request)
	blog.commit()
	return blog


def show(id, db:Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id).first()
	return blog

# Users


def create_user(user: schemas.User, db:Session):
	new_user = models.User(name = user.name,
							email = user.email,
							password = Hash.bcrypt(user.password))
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user

def show(id, db:Session):
	user = db.query(models.User).filter(models.User.id == id).first()
	return user
