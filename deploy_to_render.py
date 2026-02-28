#!/usr/bin/env python3
"""
Auto-deploy WMS_CanThongMinh to Render
Usage: python deploy_to_render.py <RENDER_API_KEY>
"""

import os
import sys
import requests
import time

GITHUB_REPO = "vuongcris4/WMS_CanThongMinh"
SERVICE_NAME = "wms-canthongminh"
REGION = "singapore"
PLAN = "free"

def create_render_service(api_key):
    """Create a new web service on Render"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Create web service - using correct API format
    service_data = {
        "name": SERVICE_NAME,
        "type": "web",
        "env": "python",
        "region": REGION,
        "repo": {
            "url": f"https://github.com/{GITHUB_REPO}",
            "branch": "main"
        },
        "buildCommand": "pip install -r requirements.txt",
        "startCommand": "gunicorn can_thong_minh.wsgi:application --bind 0.0.0.0:$PORT",
        "autoDeploy": True,
        "envVars": [
            {"key": "PYTHON_VERSION", "value": "3.12.0"},
            {"key": "DEBUG", "value": "False"},
            {"key": "WEB_CONCURRENCY", "value": "4"}
        ]
    }
    
    print("🚀 Creating Render service...")
    response = requests.post(
        "https://api.render.com/v1/services",
        headers=headers,
        json=service_data
    )
    
    if response.status_code == 400:
        print(f"Debug: {response.text}")
    
    if response.status_code == 201:
        service = response.json()
        print(f"✅ Service created: {service['name']}")
        print(f"📊 Service ID: {service['id']}")
        return service
    else:
        print(f"❌ Failed to create service: {response.text}")
        return None

def create_postgresql(api_key, service_id):
    """Create PostgreSQL database and attach to service"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    db_data = {
        "name": f"{SERVICE_NAME}-db",
        "databaseName": "can_thong_minh",
        "plan": "free",
        "region": REGION
    }
    
    print("🗄️  Creating PostgreSQL database...")
    response = requests.post(
        "https://api.render.com/v1/databases",
        headers=headers,
        json=db_data
    )
    
    if response.status_code == 201:
        db = response.json()
        print(f"✅ Database created: {db['name']}")
        
        # Get database connection string
        db_id = db['id']
        time.sleep(2)  # Wait for DB to be ready
        
        # Update service with DATABASE_URL
        service_env_data = {
            "envVars": [
                {"key": "DATABASE_URL", "value": f"postgres://render:password@{db_id}.pg.databases.render:5432/can_thong_minh"}
            ]
        }
        
        print("🔗 Connecting database to service...")
        # This would need additional API calls to update service env vars
        return db
    else:
        print(f"❌ Failed to create database: {response.text}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python deploy_to_render.py <RENDER_API_KEY>")
        print("\nGet your API key from: https://dashboard.render.com/u/settings#api-keys")
        sys.exit(1)
    
    api_key = sys.argv[1]
    
    print(f"🎯 Deploying {GITHUB_REPO} to Render...")
    print(f"📍 Region: {REGION}")
    print(f"💰 Plan: {PLAN}")
    print()
    
    # Create service
    service = create_render_service(api_key)
    if not service:
        sys.exit(1)
    
    # Create database
    db = create_postgresql(api_key, service['id'])
    
    print()
    print("=" * 50)
    print("✅ Deployment started!")
    print(f"🌐 Service URL: https://{SERVICE_NAME}.onrender.com")
    print(f"📊 Dashboard: https://dashboard.render.com")
    print()
    print("⏳ First deployment takes 5-10 minutes...")
    print("💡 Add DATABASE_URL to environment variables in Render dashboard")

if __name__ == "__main__":
    main()
