from pydantic import BaseModel

class ArticleBase(BaseModel):
  title: str
  content: str
  published: bool
  creator_id: int

# User inside ArticleDisplay
class User(BaseModel):
  id: int
  username: str
  class Config():
    from_attributes = True

class ArticleDisplay(BaseModel):
  title: str
  content: str
  published: bool
  user: User
  class Config():
    from_attributes = True