#!/usr/bin/env python3
import requests
import json

API_KEY = "rnd_DjNQp3CihyCO0PoHjOKIP44k3Hix"
OWNER_ID = "tea-d6hee424d50c73f9k93g"

payload = {
    "name": "wms-canthongminh",
    "type": "web_service",
    "env": "python",
    "region": "singapore",
    "ownerId": OWNER_ID,
    "repo": {
        "url": "https://github.com/vuongcris4/WMS_CanThongMinh",
        "branch": "main"
    },
    "buildCommand": "pip install -r requirements.txt",
    "startCommand": "gunicorn can_thong_minh.wsgi:application --bind 0.0.0.0:$PORT",
    "autoDeploy": True
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("Creating service...")
print(f"Payload: {json.dumps(payload, indent=2)}")

response = requests.post(
    "https://api.render.com/v1/services",
    headers=headers,
    data=json.dumps(payload)
)

print(f"\nStatus: {response.status_code}")
print(f"Response: {response.text}")
