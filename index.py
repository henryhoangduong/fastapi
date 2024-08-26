from fastapi import FastAPI, APIRouter
import requests
import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

router = APIRouter()

@router.get('/')
def root():
    return {'message':'hello world'}

@router.post('/container/execution')
def execute():
    heroku_api_key = os.getenv("HEROKU_KEY")
    heroku_app_name = "testone"  # Replace with your Heroku app name
    
    url = f"https://api.heroku.com/apps/{heroku_app_name}/formation"
    headers = {
        "Authorization": f"Bearer {heroku_api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    payload = {
        "updates": [
            {
                "type": "worker",
                "quantity": 1 
            }
        ]
    }
    
    response = requests.patch(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Worker dyno started successfully")
    else:
        print(f"Error starting worker dyno: {response.json()}")
    


app = FastAPI()
app.include_router(router)