from fastapi import FastAPI, APIRouter
import logging
import os
import subprocess
import heroku3
import pickle as pkl

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

router = APIRouter()


@router.get("/")
def root():
    return {"message": "hello world"}


@router.get("/app/creation")
def create_app(name: str = ""):
    logging.info(f"name: {name}")
    try:
        logging.info("Creating app......")
        response = subprocess.run(
            ["heroku", "create", "--stack", "container", name, "--team", "asol-devops"],
            capture_output=True,
            text=True,
        )
        result = response
        return {"message": "succesful", "data": {result}}
    except Exception as e:
        logging.error(f"Error creating apps: {e}")
        return {"Error": e}


@router.get("/app/name")
def get_app_name():
    logging.info("Getting key....")
    heroku_api_key = os.getenv("HEROKU_API_KEY")
    logging.info(f"heroku_api_key:{heroku_api_key}")
    heroku_conn = heroku3.from_key(heroku_api_key)
    teams = heroku_conn.apps()
    result = teams
    logging.info(f"apps: {result}")
    return {"data": list(result)}


@router.get("/app/container/start")
def start_container(app_name:str):
    logging.info("Calling start_container......")
    if app_name =='':
        return {'message':'please add app_name'}
    try:
        logging.info(f'{app_name} is pulling image from registry.heroku.com')
        result = subprocess.run(['heroku','container:release','web','--app',app_name])    
        return {'message':result}
    except Exception as e:
        logging.error(f'Error while {app_name} pulling image: {e}')

@router.get('/app/one-off/start')
def start_one_off(app_name:str):
    logging.info("Calling start_container......")
    if app_name =='':
        return {'message':'please add app_name'}
    try:
        logging.info(f'{app_name} is pulling image from registry.heroku.com')
        result = subprocess.run(['heroku','run','python','index.py','abc 123',app_name])    
        return {'message':result}
    except Exception as e:
        logging.error(f'Error while {app_name} pulling image: {e}')

app = FastAPI()
app.include_router(router)
