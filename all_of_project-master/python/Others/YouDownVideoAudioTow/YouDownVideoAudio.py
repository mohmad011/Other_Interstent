from pytube import YouTube

Rerun = 'y'

while Rerun != 'n' :
	link = input("Please Inter Your Vedio Url:...\n")
	audioVideo = input("Do You Need (mp4 or mp3) :...\n")
	QualityVideo = input("Plaese Enter The Quality Video (144 or 240 or 360 or 480 or 720 or 1080) :...\n")




	# link = "https://www.youtube.com/watch?v=3W-yNYYHnpQ"

	Videos = YouTube(link)

	def finish():
		print( Videos.title +  "\nDownload Done")

	if audioVideo == 'mp4':
		try:
			print("Downloading....")
			if QualityVideo != "144" and QualityVideo != "240" and QualityVideo != "360" and QualityVideo != "480" and QualityVideo != "720" and QualityVideo != "1080":
				Videos.streams.filter(res="360p").order_by('resolution').desc().first().download(output_path="./save")
			# elif QualityVideo == "240":
			# 	Videos.streams.filter(res="240p").order_by('resolution').desc().first().download(output_path="./save")
			# elif QualityVideo == "360":
			# 	Videos.streams.filter(res="360p").order_by('resolution').desc().first().download(output_path="./save")
			# elif QualityVideo == "480":
			# 	Videos.streams.filter(res="480p").order_by('resolution').desc().first().download(output_path="./save")
			# elif QualityVideo == "720":
			# 	Videos.streams.filter(res="720p").order_by('resolution').desc().first().download(output_path="./save")
			# elif QualityVideo == "1080":
			# 	Videos.streams.filter(res="1080p").order_by('resolution').desc().first().download(output_path="./save")
				Videos.register_on_complete_callback(finish())
			else:
				Videos.streams.filter(res=QualityVideo + "p").order_by('resolution').desc().first().download(output_path="./save")
				Videos.register_on_complete_callback(finish())
		except:
			print("Downloading....")
			Videos.streams.get_lowest_resolution().download(output_path="./save")
			Videos.register_on_complete_callback(finish())
	else :

		try:
			print("Downloading....")
			Videos.streams.filter(progressive=False, only_audio=True , abr="128kbps" , type="audio").desc().download(output_path="./save")
			# for stream in Videos.streams:
			# 	print(stream)
			Videos.register_on_complete_callback(finish())
		except:
			print("Downloading....")
			Videos.streams.get_lowest_resolution().download(output_path="./save")
			Videos.register_on_complete_callback(finish())

	Rerun = input("Do You Want To Re Run Code (y or n) ?....\n")


##########################################################################################

# for stream in Videos.streams.filter(res="360p" , subtype="mp4" , type="video" , progressive=True):
# 	print(stream)

# Videos.streams.get_lowest_resolution().download(output_path="./save")

# YouTube(link).streams.filter(res="360p" , subtype="mp4" , type="video" , progressive=True).download(output_path="./save")

# YouTube('https://www.youtube.com/watch?v=3W-yNYYHnpQ').streams.first().download()

# for stream in Videos.streams:
# 	print(streamt)
	# stream.filter(res="360p" , subtype="mp4" , type="video" , progressive=True).download(output_path="./save")
	# try:
	# 	stream.filter(res="360p" , subtype="mp4" , type="video" , progressive=True).download(output_path="./save")
	# except:
	# 	stream.get_highest_resolution().download(output_path="./save")
