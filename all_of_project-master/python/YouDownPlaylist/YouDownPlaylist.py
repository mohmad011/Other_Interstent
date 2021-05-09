from pytube import Playlist

playlist_link = input("Please Inter You Playlist Link:...\n")

playlist = Playlist(playlist_link)

for video in playlist.videos:
	# video.streams.filter(res="360p" , subtype="mp4" , type="video" , progressive=True).order_by('resolution').desc().first().download(output_path="./save")
	try:
		video.streams.filter(res="360p" , subtype="mp4" , type="video" , progressive=True).order_by('resolution').desc().first().download(output_path="./save")
		print("-----------------------------------------------------------")
		print("Done")
	except:
		video.streams.get_lowest_resolution().download(output_path="./save")
		print("-----------------------------------------------------------")
		print("Done")