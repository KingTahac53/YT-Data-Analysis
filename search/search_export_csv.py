import requests
import json
import pandas as pd


def youtube_search(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "maxResults": 50,
        "q": query,
        "regionCode": "US",
        "key": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


def get_video_details(video_ids, api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "statistics,snippet",
        "id": ",".join(video_ids),
        "key": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    API_KEY = "x"
    query = "avatar movie"

    search_results = youtube_search(query, API_KEY)

    if isinstance(search_results, dict) and "items" in search_results:
        video_ids = [item["id"]["videoId"]
                     for item in search_results["items"] if "videoId" in item["id"]]
        # print(json.dumps(video_ids,indent=4))
        video_details = get_video_details(video_ids, API_KEY)

        data = []
        if isinstance(video_details, dict) and "items" in video_details:
            # print(json.dumps(video_details["items"][0],indent=4))
            for video in video_details["items"]:
                statistics = video.get("statistics", {})
                snippet = video.get("snippet", {})

                data.append({
                    "Video ID": video["id"],
                    "Title": snippet.get("title"),
                    "No of Views": statistics.get("viewCount", 0),
                    "No of Likes": statistics.get("likeCount", 0),
                    "No of Comments": statistics.get("commentCount", 0)
                })

            df = pd.DataFrame(data)
            df.to_csv("avatar_movie_statistics.csv", index=False)
            print("Data exported to avatar_movie_statistics.csv successfully")
        else:
            print("No video details found.")
    else:
        print("No data found!")
