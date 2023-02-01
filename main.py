from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/')
def get_ativos():
    return "Hello word"

app.include_router(prefix='/get_ativos', router=router)