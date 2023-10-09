from fastapi import APIRouter

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/new', summary='Create a user')
def create_user():
  pass