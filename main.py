from fastapi import FastAPI
from controllers import blog, user


app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}