from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def homepage():
    return {"request": "made"}
