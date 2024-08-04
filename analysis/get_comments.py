import requests
import pandas as pd
import json
from pprint import pprint


def read_and_sort_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        df['No of Comments'] = pd.to_numeric(
            df['No of Comments'], errors='coerce').fillna(0).astype(int)
        sorted_df = df.sort_values(by='No of Comments', ascending=False)
        top_10_videos = sorted_df.head(10)
        top_10_video_ids_titles = top_10_videos[['Video ID', 'Title']]

        return top_10_video_ids_titles
    except Exception as e:
        print(f"An error occurred: {e}")


def get_video_comments(video_id, api_key):
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": 10,
        "key": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    API_KEY = "AIzaSyB32pztkNyn6Pr4shYOr_8_AhktdxMzTDE"
    file_path = "avatar_movie_statistics.csv"

    top_10_video_ids_titles = read_and_sort_csv(file_path)

    for index, row in top_10_video_ids_titles.iterrows():
        video_id = row['Video ID']
        print(f"\nComments for video ID: {video_id} ({row['Title']}):")
        comments = get_video_comments(video_id, API_KEY)
        # pprint(json.dumps(comments, indent=4))
        pprint(comments)
