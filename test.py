import heroku3
from dotenv import load_dotenv
import os 

load_dotenv()

HEROKU_KEY = os.getenv('HEROKU_KEY')
HEROKU_KEY = os.getenv('HEROKU_KEY')


import requests
import os

def start_worker_dyno():
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

start_worker_dyno()