import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ORS_API_KEY")

print("API KEY:", API_KEY)

headers = {
    "Authorization": API_KEY
}

params = {
    "text": "New York",
    "size": 1
}

response = requests.get(
    "https://api.openrouteservice.org/geocode/search",
    headers=headers,
    params=params
)

print(response.status_code)

print(response.json())