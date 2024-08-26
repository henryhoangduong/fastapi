from fastapi import FastAPI, APIRouter
import docker
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

router = APIRouter()

@router.get('/')
def root():
    return {'message':'hello world'}

@router.post('/container/execution')
def execute():
    logging.info('Recieved execution request')
    try:
        logging.info('Initializing container')
        client = docker.from_env()
    except Exception as e:
        logging.error(f'Error initializing container client: {e}')


app = FastAPI()
app.include_router(router)