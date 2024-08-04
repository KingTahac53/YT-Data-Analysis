# -*- coding: utf-8 -*-

import time
import googleapiclient.discovery
import googleapiclient.errors


def main():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key
    )

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics", id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    )

    # Implementing retries with exponential backoff
    retries = 5
    for i in range(retries):
        try:
            response = request.execute()
            print(response)
            break
        except googleapiclient.errors.HttpError as err:
            print(f"HttpError: {err}")
            if i < retries - 1:
                time.sleep(2**i)  # Exponential backoff
            else:
                raise
        except TimeoutError as err:
            print(f"TimeoutError: {err}")
            if i < retries - 1:
                time.sleep(2**i)  # Exponential backoff
            else:
                raise


if __name__ == "__main__":
    main()
