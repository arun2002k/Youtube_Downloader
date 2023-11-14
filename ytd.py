import pytube

video_url = input("Wreite your video url : ")
yt = pytube.YouTube(video_url)
stream = yt.streams.get_highest_resolution()
print("Video is downloading....")
stream.download()