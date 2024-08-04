import pandas as pd

def read_and_sort_csv(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Ensure 'No of Comments' column is of integer type
        df['No of Comments'] = pd.to_numeric(df['No of Comments'], errors='coerce').fillna(0).astype(int)
        
        # Sort the DataFrame by 'No of Comments' in descending order
        sorted_df = df.sort_values(by='No of Comments', ascending=False)
        
        # Get the top 10 videos with the highest number of comments
        top_10_videos = sorted_df.head(10)
        
        # Extract the video IDs and titles of the top 10 videos
        top_10_video_ids_titles = top_10_videos[['Video ID', 'Title']]
        
        # Print the top 10 video IDs and titles
        print("Top 10 videos with the highest number of comments:")
        print(top_10_video_ids_titles)
        
        return top_10_video_ids_titles
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "avatar_movie_statistics.csv"  # Replace with your actual CSV file path
    top_10_video_ids_titles = read_and_sort_csv(file_path)
    
    # Optional: Export the top 10 videos to a new CSV file
    top_10_video_ids_titles.to_csv("top_10_videos_by_comments.csv", index=False)
    print("Top 10 videos data exported to top_10_videos_by_comments.csv successfully")
