from typing import List
from pydantic import BaseModel


# Article inside UserDisplay
class Article(BaseModel):
  title: str
  content: str
  published: bool
  class Config():
    from_attributes = True
class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  items: List[Article] = []
  class Config():
    from_attributes = True

