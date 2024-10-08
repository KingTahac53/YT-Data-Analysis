# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_889524826764-a2d418hn7ooki7gd76145cotqemkonfl.apps.googleusercontent.com.json"
    print(client_secrets_file, "Deee")

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    print(flow)
    credentials = flow.run_local_server(
        port=0
    )  # Changed from run_console() to run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics", id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
