from fastapi import FastAPI, APIRouter
import logging
import os
import subprocess
import heroku3
import re
import pickle as pkl

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

router = APIRouter()


@router.get("/")
def root():
    return {"message": "hello world"}


@router.get("/syscall")
def syscall():
    heroku_api_key = os.getenv("HEROKU_API_KEY")
    print("heroku_api_key: ", heroku_api_key)
    try:
        result = subprocess.run(["heroku", "whoami"], capture_output=True, text=True)
        print("result: ", result)
    except Exception as e:
        print(f"Error login with heroku: {e}")


@router.get("/syscallwithshell")
def syscallwithshell():
    subprocess.run(["sh", "heroku.sh"])


@router.get("/createapp")
def syscallwithshell():
    try:
        logging.info("Creating app......")
        response = subprocess.run(
            ["heroku", "create", "--stack", "container", "--team", "asol-devops"],
            capture_output=True,
            text=True,
        )
        result = response
        return {"message": "succesful", "data": {result}}
    except Exception as e:
        logging.error(f"Error creating apps: {e}")
        return {'Error':e}


@router.get("/appname")
def get_app_name():
    logging.info('Getting key....')
    heroku_api_key = os.getenv("HEROKU_API_KEY")
    logging.info(f'heroku_api_key:{heroku_api_key}')
    heroku_conn = heroku3.from_key(heroku_api_key)
    teams = heroku_conn.apps()
    result = teams
    logging.info(f'apps: {result}')
    return {'data':list(result)}

def clean_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def parse_output(text):
    cleaned_text = clean_ansi_escape_sequences(text)
    lines = cleaned_text.splitlines()
    return lines

app = FastAPI()
app.include_router(router)
