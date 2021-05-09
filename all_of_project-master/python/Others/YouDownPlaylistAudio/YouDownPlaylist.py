from pytube import Playlist

playlist_link = input("Please Inter You Playlist Link:...\n")

playlist = Playlist(playlist_link)

for video in playlist.videos:
	def finish():
		print("Download Done")
	# video.streams.filter(res="360p" , subtype="mp4" , type="video" , progressive=True).order_by('resolution').desc().first().download(output_path="./save")
	try:
		video.streams.filter(progressive=False, only_audio=True , abr="128kbps" , type="audio").first().download(output_path="./save")
		video.register_on_complete_callback(finish())
	except:
		video.streams.get_lowest_resolution().download(output_path="./save")
		video.register_on_complete_callback(finish())