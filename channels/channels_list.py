# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import googleapiclient.discovery
import googleapiclient.errors
import json

def main():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyB32pztkNyn6Pr4shYOr_8_AhktdxMzTDE"

    # Create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()

    print(json.dumps(response,indent=4))

if __name__ == "__main__":
    main()
