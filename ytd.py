# Importing python package 
import pytube

# Paste the youtube video url 
video_url = input("Write your video url : ")
yt = pytube.YouTube(video_url)

# Getting the video in HD format
stream = yt.streams.get_highest_resolution()

# Video is downloading and stored in your pc
print("Video is downloading....")
stream.download() #provide path to a specific folder using ''
print("Video downloaded!!!!..")
