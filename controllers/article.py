from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.models.article_model import ArticleBase, ArticleDisplay
from controllers.models.user_model import UserBase
from db.database import get_db
from db.repositories import db_article
from helpers.oauth2 import get_current_user

router = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return db_article.create_article(db, request)

# Get specific article
@router.get('/{id}') #, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return {
    'data': db_article.get_article(db, id),
    'current_user': current_user
  }