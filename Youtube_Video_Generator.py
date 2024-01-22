from pytube import YouTube

def download_video(video_url, save_path="."):
    try:
        # Create a YouTube object
        youtube = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = youtube.streams.get_highest_resolution()

        # Register the callback function to track download progress
        video_stream.register_on_progress_callback(on_progress)

        # Download the video
        video_stream.download(save_path)

        print("\nDownload completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def on_progress(stream, chunk, bytes_remaining):
    # Calculate the percentage of downloaded bytes
    percent = round((1 - bytes_remaining / stream.filesize) * 100, 2)
    print(f"\rDownloading: {percent}% complete", end="")

if __name__ == "__main__":
    # Get the YouTube video URL from the user
    video_url = input("Enter the YouTube video URL: ")

    # Specify the folder where the video will be saved (default is the current working directory)
    save_path = input("Enter the path to save the video (press Enter to save in the current directory): ")

    # Download the video
    download_video(video_url, save_path)
