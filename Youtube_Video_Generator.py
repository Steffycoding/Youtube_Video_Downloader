from pytube import YouTube
from tkinter import filedialog, Tk, simpledialog
from colorama import Fore, Style

def get_video_streams(video):
    streams = video.streams.filter(progressive=True).order_by('resolution').desc()
    return streams

def display_available_streams(streams):
    print("\nAvailable Video Resolutions:")
    for i, stream in enumerate(streams, start=1):
        print(f"{i}. {stream.resolution} - {stream.mime_type}")

def get_user_choice():
    # Prompt user to select a stream
    choice = simpledialog.askinteger("Video Quality", "Enter the number corresponding to the desired video quality:")
    return choice

def download_video(video_url):
    try:
        # Create a YouTube object
        youtube = YouTube(video_url)

        # Get available video streams
        video_streams = get_video_streams(youtube)

        # Display available video streams
        display_available_streams(video_streams)

        # Prompt user to select a stream
        choice = get_user_choice()
        selected_stream = video_streams[choice - 1]

        # Choose the destination folder interactively
        Tk().withdraw()  # Close the root window
        destination_folder = filedialog.askdirectory(title="Select Destination Folder")

        # Download the video
        print(f"\nDownloading in {selected_stream.resolution} quality to {destination_folder}...")
        selected_stream.download(destination_folder)

        print(Fore.LIME + Style.BRIGHT + "\nDOWNLOAD COMPLETED SUCCESSFULLY!" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"\nAN ERROR OCCURRED: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    # Get the YouTube video URL from the user
    video_url = input("Enter the YouTube video URL: ")

    # Download the video
    download_video(video_url)
