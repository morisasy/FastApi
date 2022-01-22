from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class Blog(BaseModel):
	title: str 
	body: str 
	published: Optional[bool]


@app.get("/api")
def index():
	return {'data': "Hey perkele!"}

@app.get("/api/about")
def about():
	return {'data': "About page"}


@app.get("/api/blog")
def blog(limit =10, published: bool = True, sort: Optional[str] = None):
	# only published 10 blog
	# display blog list
	if published:
		return {'data': f"{limit} published blogs from the db"}
	else:
		return {'data': f"{limit} blogs from the db"} 
	


@app.get("/api/blog/{id}")
def blog_id(id: int):
	# fetch blog with id = id
	return {'data': id}



@app.get("/api/blog/unpublished")
def unpublished():
	# display blog list
	return {'data': "All unpublished blogs"}


@app.get("/api/blog/{id}/comments")
def comments(id, limit=10):
	# fetch comments of blog with id = id
	return {'data': id}

@app.post("/api/blog")
def create_blog(blog: Blog):
	# a blog of type Blog
	return {'data': f"Blog is created with title as {blog.title}"}



#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")





