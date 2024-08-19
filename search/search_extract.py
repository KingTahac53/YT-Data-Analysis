import requests
import json


def youtube_search(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {"part": "snippet", "maxResults": 25, "q": query, "key": api_key}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    API_KEY = "xxxxxxx"
    query = "avatar movie"

    search_results = youtube_search(query, API_KEY)

    if isinstance(search_results, dict) and "items" in search_results:
        video_data = search_results["items"][5]
        output = (
            {
                "ID": video_data["id"]["videoId"],
                "Snippet": {
                    "Channel ID": video_data["snippet"]["channelId"],
                    "Video Description": video_data["snippet"]["description"],
                    "Channel Title": video_data["snippet"]["channelTitle"],
                    "Video Title": video_data["snippet"]["title"],
                },
            },
        )
        print(json.dumps(output, indent=4))
    else:
        print("Unable to find data")
