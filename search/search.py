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
    API_KEY = "xxxxxxx"  # Replace with your YouTube Data API v3 key
    query = "avatar movie"

    results = youtube_search(query, API_KEY)

    # Check if the results are a dictionary (indicating a successful API response)
    if isinstance(results, dict):
        # Save the response in a JSON file
        with open("youtube_search_results.json", "w") as json_file:
            json.dump(results, json_file, indent=4)
        print("Response saved to youtube_search_results.json")
    else:
        print(results)
