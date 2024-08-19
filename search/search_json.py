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


def get_video_details(video_id, api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"part": "snippet", "id": video_id, "key": api_key}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    # Replace with your YouTube Data API v3 key
    API_KEY = "xxxxxxx"
    query = "avatar movie"

    # Step 1: Search for videos related to the query
    search_results = youtube_search(query, API_KEY)

    # Step 2: Choose one video from the search results
    if isinstance(search_results, dict) and "items" in search_results:
        # Select the first video from the search results
        video_id = search_results["items"][0]["id"]["videoId"]

        # Step 3: Get detailed information about the selected video
        video_details = get_video_details(video_id, API_KEY)

        # Extract the required information
        if (
            isinstance(video_details, dict)
            and "items" in video_details
            and video_details["items"]
        ):
            video_info = video_details["items"][0]
            output = {
                "ID": video_info["id"],
                "Snippet": video_info["snippet"],
                "Channel ID": video_info["snippet"]["channelId"],
                "Video Description": video_info["snippet"]["description"],
                "Channel Title": video_info["snippet"]["channelTitle"],
                "Video Title": video_info["snippet"]["title"],
            }
            print(json.dumps(output, indent=4))

            # Optionally, save the output to a JSON file
            with open("video_info.json", "w") as json_file:
                json.dump(output, json_file, indent=4)
            print("Video information saved to video_info.json")
        else:
            print("No video details found.")
    else:
        print(search_results)
