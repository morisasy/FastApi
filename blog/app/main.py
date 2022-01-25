# main.py

from fastapi import FastAPI

from blog.routers import  blog, user, authentication
#from .. import schemas, database, models, oauth2
from blog import models, database
#from blog import enginegi



app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
