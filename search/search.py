import requests
import json


def youtube_search(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {"part": "snippet", "maxResults": 25, "q": query, "key": api_key}

    try:
        response = requests.get(url, params=params, timeout=10)  # 10 seconds timeout
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    API_KEY = "AIzaSyB32pztkNyn6Pr4shYOr_8_AhktdxMzTDE"  # Replace with your YouTube Data API v3 key
    query = "surfing"

    results = youtube_search(query, API_KEY)

    # Print the response in a pretty JSON format
    if isinstance(results, dict):
        print(json.dumps(results, indent=4))
    else:
        print(results)
