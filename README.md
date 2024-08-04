YouTube Data API Analysis
This repository contains various scripts and tools for analyzing YouTube data using the YouTube Data API v3. The project is divided into several folders, each containing scripts for different tasks such as searching videos, fetching video statistics, retrieving comments, and exporting data.

Table of Contents
Installation
Usage
Video Search
Video Statistics
Comment Retrieval
Likes vs Views Ratio
Scripts Overview
License
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/internet-monitor.git
cd internet-monitor
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Video Search
The script to search for videos based on a query and export the results is located in the video_search folder.

Example usage:
python
Copy code
import requests
import json

def youtube_search(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {"part": "snippet", "maxResults": 50, "q": query, "regionCode": "US", "key": api_key}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    query = "avatar movie"
    search_results = youtube_search(query, API_KEY)
    with open("search_results.json", "w") as json_file:
        json.dump(search_results, json_file, indent=4)
    print("Search results saved to search_results.json")
Video Statistics
The script to fetch video statistics and export them to a CSV file is located in the video_statistics folder.

Example usage:
python
Copy code
import requests
import pandas as pd

def get_video_statistics(video_ids, api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"part": "statistics,snippet", "id": ",".join(video_ids), "key": api_key}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    video_ids = ["video_id_1", "video_id_2", ...]
    video_statistics = get_video_statistics(video_ids, API_KEY)
    data = []
    for video in video_statistics["items"]:
        statistics = video["statistics"]
        snippet = video["snippet"]
        data.append({"Video ID": video["id"], "Title": snippet["title"], "Views": statistics["viewCount"], "Likes": statistics["likeCount"], "Comments": statistics["commentCount"]})
    df = pd.DataFrame(data)
    df.to_csv("video_statistics.csv", index=False)
    print("Video statistics saved to video_statistics.csv")
Comment Retrieval
The script to retrieve comments for the top 10 videos with the highest comments is located in the comments_retrieval folder.

Example usage:
python
Copy code
import requests
import pandas as pd
import json
from pprint import pprint

def get_video_comments(video_id, api_key):
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {"part": "snippet", "videoId": video_id, "maxResults": 10, "key": api_key}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    file_path = "avatar_movie_statistics.csv"
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by='No of Comments', ascending=False).head(10)
    video_ids = df_sorted["Video ID"].tolist()
    comments_data = {}
    for video_id in video_ids:
        comments = get_video_comments(video_id, API_KEY)
        comments_data[video_id] = comments
        pprint(comments)
    with open("top_10_video_comments.json", "w") as json_file:
        json.dump(comments_data, json_file, indent=4)
    print("Comments data saved to top_10_video_comments.json")
Likes vs Views Ratio
The script to calculate the likes vs views ratio for the top 10 videos with the highest comments is located in the likes_vs_views_ratio folder.

Example usage:
python
Copy code
import requests
import pandas as pd

def get_video_statistics(video_ids, api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"part": "statistics", "id": ",".join(video_ids), "key": api_key}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def calculate_likes_vs_views_ratio(video_statistics):
    ratios = {}
    for video in video_statistics.get("items", []):
        video_id = video["id"]
        view_count = int(video["statistics"].get("viewCount", 0))
        like_count = int(video["statistics"].get("likeCount", 0))
        ratio = like_count / view_count if view_count > 0 else 0
        ratios[video_id] = ratio
    return ratios

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    file_path = "avatar_movie_statistics.csv"
    df = pd.read_csv(file_path)
    df_sorted = df.sort_values(by='No of Comments', ascending=False).head(10)
    video_ids = df_sorted["Video ID"].tolist()
    video_statistics = get_video_statistics(video_ids, API_KEY)
    ratios = calculate_likes_vs_views_ratio(video_statistics)
    for video_id, ratio in ratios.items():
        title = df_sorted.loc[df_sorted["Video ID"] == video_id, "Title"].values[0]
        print(f"Video ID: {video_id}, Title: {title}, Likes vs Views Ratio: {ratio:.4f}")
Scripts Overview
Folders and Scripts
video_search/:

youtube_search.py: Script to search videos based on a query and export the results to a JSON file.
video_statistics/:

get_video_statistics.py: Script to fetch video statistics (views, likes, comments) and export them to a CSV file.
comments_retrieval/:

get_video_comments.py: Script to retrieve comments for the top 10 videos with the highest comments and export them to a JSON file.
likes_vs_views_ratio/:

calculate_likes_vs_views_ratio.py: Script to calculate the likes vs views ratio for the top 10 videos with the highest comments.
License
This project is licensed under the MIT License - see the LICENSE file for details.

