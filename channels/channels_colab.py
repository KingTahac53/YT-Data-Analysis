import os
import json
import google.auth
from google.colab import auth
from googleapiclient.discovery import build

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    auth.authenticate_user()
    credentials, project = google.auth.default(scopes=scopes)
    
    api_service_name = "youtube"
    api_version = "v3"
    
    youtube = build(api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics", mine=True
    )
    response = request.execute()

    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    main()
