from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)

@app.get("/")
def index():
    return {"message": "Hello World!"}

@app.get("/api")
async def get_info(slack_name: str, track: str):
    # Validate slack_name and track_name
    if not slack_name or not track:
        raise HTTPException(status_code=400, detail="slack_name and track_name are required")

    # Get the current day of the week
    current_day_of_week = datetime.utcnow().strftime("%A")

    # Get the current UTC time with validation of +/-2 hours
    current_utc_time = datetime.utcnow()
    current_utc_time_str = str(current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ"))

    # Replace these with your actual GitHub URLs
    source_code_github_url = "https://github.com/Zainabfadeyi/Hng/blob/main/main.py"
    file_github_url = "https://github.com/Zainabfadeyi/Hng"
    

    # Create the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day_of_week,
        "utc_time": current_utc_time_str,
        "track": track,
        "github_file_url": source_code_github_url,
        "github_repo_url": file_github_url,
        "status_code": 200
    }

    return response_data