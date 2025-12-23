import requests, os
from dotenv import load_dotenv

load_dotenv()

url = "https://maps.googleapis.com/maps/api/geocode/json"
params = {
    "address": "Gateway of India Mumbai",
    "key": os.getenv("GOOGLE_MAPS_API_KEY")
}

res = requests.get(url, params=params)
print(res.json())
