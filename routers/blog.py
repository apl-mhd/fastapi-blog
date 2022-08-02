from fastapi import APIRouter
from .. blog import schemas
from typing import List

router = APIRouter

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs