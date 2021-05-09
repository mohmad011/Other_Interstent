from pytube import Playlist

Rerun = 'y'

while Rerun != 'n' :

	playlist_link = input("Please Inter You Playlist Link:...\n")
	audioVideo = input("Do You Need (mp4 or mp3) :...\n")
	QualityVideo = input("Plaese Enter The Quality Video (144 or 240 or 360 or 480 or 720 or 1080) :...\n")
	playlist = Playlist(playlist_link)

	for video in playlist.videos:
		# video.streams.filter(res="360p" , subtype="mp4" , type="video" , progressive=True).order_by('resolution').desc().first().download(output_path="./save")

		def finish():
			print( video.title +  "\nDownload Done")

		if audioVideo == 'mp4':

			try:
				print("Downloading....")
				if QualityVideo != "144" and QualityVideo != "240" and QualityVideo != "360" and QualityVideo != "480" and QualityVideo != "720" and QualityVideo != "1080":
					video.streams.filter(res="360p").order_by('resolution').desc().first().download(output_path="./save")
				# elif QualityVideo == "240":
				# 	video.streams.filter(res="240p").order_by('resolution').desc().first().download(output_path="./save")
				# elif QualityVideo == "360":
				# 	video.streams.filter(res="360p").order_by('resolution').desc().first().download(output_path="./save")
				# elif QualityVideo == "480":
				# 	video.streams.filter(res="480p").order_by('resolution').desc().first().download(output_path="./save")
				# elif QualityVideo == "720":
				# 	video.streams.filter(res="720p").order_by('resolution').desc().first().download(output_path="./save")
				# elif QualityVideo == "1080":
				# 	video.streams.filter(res="1080p").order_by('resolution').desc().first().download(output_path="./save")
					video.register_on_complete_callback(finish())
				else:
					video.streams.filter(res=QualityVideo + "p").order_by('resolution').desc().first().download(output_path="./save")
					video.register_on_complete_callback(finish())
			except:
				print("Downloading....")
				video.streams.get_lowest_resolution().download(output_path="./save")
				video.register_on_complete_callback(finish())	
		else:

			try:
				print("Downloading....")
				video.streams.filter(progressive=False, only_audio=True , abr="128kbps" , type="audio").first().download(output_path="./save")
				video.register_on_complete_callback(finish())
				# print(os.listdir("."))

			except:
				print("Downloading....")
				video.streams.get_lowest_resolution().download(output_path="./save")
				video.register_on_complete_callback(finish())
				# print(os.listdir("."))
	Rerun = input("Do You Want To Re Run Code (y or n) ?....\n")