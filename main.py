from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import requests

app = FastAPI()

@app.get("/api")
async def get_info(slack_name: str, track_name: str):
    # Validate slack_name and track_name
    if not slack_name or not track_name:
        raise HTTPException(status_code=400, detail="slack_name and track_name are required")

    # Get the current day of the week
    current_day_of_week = datetime.utcnow().strftime("%A")

    # Get the current UTC time with validation of +/-2 hours
    current_utc_time = datetime.utcnow()
    utc_offset = timedelta(hours=2)  # Adjust the offset as needed
    current_utc_time += utc_offset
    current_utc_time_str = current_utc_time.strftime("%Y-%m-%d %H:%M:%S")

    # Replace these with your actual GitHub URLs
    file_github_url = "https://github.com/Zainabfadeyi/Hng"
    source_code_github_url = "https://github.com/Zainabfadeyi/Hng/blob/main/main.py"

    # Create the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day_of_week": current_day_of_week,
        "current_utc_time": current_utc_time_str,
        "track": track_name,
        "file_github_url": file_github_url,
        "source_code_github_url": source_code_github_url,
        "status_code": 200
    }

    return response_data