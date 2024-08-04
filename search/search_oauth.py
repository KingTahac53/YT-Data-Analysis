import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "../client_secret_889524826764-a2d418hn7ooki7gd76145cotqemkonfl.apps.googleusercontent.com.json"

    try:
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes
        )
        credentials = flow.run_local_server(port=8080)

        print("Credentials obtained successfully.")

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials
        )

        print("YouTube API client created successfully.")

        request = youtube.search().list(part="snippet", maxResults=25, q="surfing")

        print("API request created successfully.")

        response = request.execute()

        print("API request executed successfully.")
        print(response)

    except googleapiclient.errors.HttpError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
