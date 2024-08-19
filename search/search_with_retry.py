import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def youtube_search(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {"part": "snippet", "maxResults": 2, "q": query, "key": api_key}

    # Configure retry strategy
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    try:
        response = http.get(url, params=params, timeout=10)  # 10 seconds timeout
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    API_KEY = "xxxxxxx"  # Replace with your YouTube Data API v3 key
    query = "surfing"

    results = youtube_search(query, API_KEY)

    # Print the response in a pretty JSON format
    if isinstance(results, dict):
        print(json.dumps(results, indent=4))
    else:
        print(results)
