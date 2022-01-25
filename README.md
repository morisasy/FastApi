# FastAIP

## Endpoints

- GET - GET an information
- POST - CREATE something new
- PUT - update
- DELETE - DELETE something


### run server

- uvicorn main:app --reload

#### installation

- pip install fastapi
- pip install "uvicorn[standard]"
- from fastapi import FastAPI, Path
- from typing import Optional
- from pydantic import BaseModel
- import uvicorn

#### requirements.txt
- fastapi

- uvicorn

- sqlalchemy

- passlib

- bcrypt

- starlette

- python-jose

python-multipart

#### check

- http://127.0.0.1:8000/docs

### Deploy on Deta
- https://web.deta.sh/

#### Blog
- https://fvgavm.deta.dev/docs
