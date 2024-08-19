import requests
import pandas as pd
import json


def read_and_sort_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        df["No of Comments"] = (
            pd.to_numeric(df["No of Comments"], errors="coerce").fillna(0).astype(int)
        )
        sorted_df = df.sort_values(by="No of Comments", ascending=False)
        top_10_videos = sorted_df.head(10)
        top_10_video_ids_titles = top_10_videos[["Video ID", "Title"]]

        return top_10_video_ids_titles
    except Exception as e:
        print(f"An error occurred: {e}")


def get_video_statistics(video_ids, api_key):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"part": "statistics", "id": ",".join(video_ids), "key": api_key}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"


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
    # Replace with your actual API key
    API_KEY = "xxxxxxx"
    # Path to the CSV file generated earlier
    file_path = "avatar_movie_statistics.csv"

    # Read and sort CSV
    top_10_video_ids_titles = read_and_sort_csv(file_path)

    # Get video IDs
    video_ids = top_10_video_ids_titles["Video ID"].tolist()

    # Get video statistics
    video_statistics = get_video_statistics(video_ids, API_KEY)

    # Calculate likes vs views ratio
    likes_vs_views_ratios = calculate_likes_vs_views_ratio(video_statistics)

    # Print the ratios
    for video_id, ratio in likes_vs_views_ratios.items():
        title = top_10_video_ids_titles.loc[
            top_10_video_ids_titles["Video ID"] == video_id, "Title"
        ].values[0]
        print(
            f"Video ID: {video_id}, Title: {title}, Likes vs Views Ratio: {ratio:.4f}"
        )
