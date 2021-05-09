# sudo pip3 install git+https://github.com/pytube/pytube

from pytube import YouTube

link = input("Please Inter Your Vedio Url:...\n")

Vedios = YouTube(link)

# print("The Vedios Title Is:\n{Vedios.title}\n--------------")
# print("The Vedios Description Is:\n{Vedios.description}\n--------------")
# print("The Vedios Views Is:\n{Vedios.views}\n--------------")
# print("The Vedios Rating Is:\n{Vedios.rating}\n--------------")
# print("The Vedios Duration Is:\n{Vedios.duration} Seconds \n--------------")

# print(Vedios.streams)

# for stream in Vedios.streams:
# 	print(stream)

# for stream in Vedios.streams.filter(progressive=True):
# 	print(stream)

# for stream in Vedios.streams.filter(progressive=True , res="360p"):
# 	print(stream)

# for stream in Vedios.streams.filter(subtype="mp4" , res="360p"):
# 	print(stream)

# print(Vedios.streams.get_highest_resolution())

# print(Vedios.streams.get_lowest_resolution())

# def finish():
# 	print("Download Done")


# Vedios.streams.get_lowest_resolution.download(output="/Desktop" , filename="mohmad gamal")

# Vedios.register_on_complete_callback(finish())

# from pytube import Playlist

# playlist_link = input("Please Inter You Playlist Link:...\n")

# playlist = Playlist(playlist_link)

# for video in playlist.videos:
# 	video.streams.get_lowest_resolution().download(output="/Desktop")