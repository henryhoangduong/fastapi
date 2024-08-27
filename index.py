from fastapi import FastAPI, APIRouter
import requests
import logging
import os
import subprocess

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

router = APIRouter()

@router.get('/')
def root():
    return {'message':'hello world'}

@router.get('/syscall')
def syscall():
    heroku_api_key = os.getenv('HEROKU_API_KEY')
    print('heroku_api_key: ', heroku_api_key)
    try:
        result = subprocess.run(['heroku', 'whoami'], capture_output=True, text=True)
        print('result: ', result)
    except Exception as e:
        print(f'Error login with heroku: {e}')

@router.get('/syscallwithshell')
def syscallwithshell():
    subprocess.run(['sh','heroku.sh'])


app = FastAPI()
app.include_router(router)