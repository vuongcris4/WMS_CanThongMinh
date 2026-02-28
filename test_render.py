#!/usr/bin/env python3
import requests
import json

API_KEY = "rnd_3UoPh4JykemACtycRouDHupXlefb"
OWNER_ID = "tea-d6hee424d50c73f9k93g"

# Create Blueprint instead - uses render.yaml from repo
blueprint_payload = {
    "name": "wms-canthongminh-blueprint",
    "ownerId": OWNER_ID,
    "repo": {
        "url": "https://github.com/vuongcris4/WMS_CanThongMinh",
        "branch": "main"
    },
    "renderYamlPath": "render.yaml"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

print("Creating Blueprint on Render...")
print()

response = requests.post(
    "https://api.render.com/v1/blueprints",
    headers=headers,
    data=json.dumps(blueprint_payload)
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 201:
    print("\n✅ Blueprint created!")
    blueprint = response.json()
    print(f"Blueprint ID: {blueprint.get('id')}")
else:
    print(f"\n❌ Failed")
    print("Trying direct deploy link instead...")
    print("\n👉 Click this link to deploy:")
    print("https://render.com/deploy?repo=https://github.com/vuongcris4/WMS_CanThongMinh")
