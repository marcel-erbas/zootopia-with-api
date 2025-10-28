import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_NINJAS_KEY")


def fetch_animals(name):
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL, headers=headers, params={"name": name})
    response.raise_for_status()
    return response.json()