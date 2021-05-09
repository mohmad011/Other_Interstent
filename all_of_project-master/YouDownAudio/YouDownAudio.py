from pytube import YouTube

link = input("Please Inter Your Vedio Url:...\n")

# link = "https://www.youtube.com/watch?v=3W-yNYYHnpQ"

Videos = YouTube(link)

# for stream in Videos.streams:
# 	print(stream)

def finish():
	print("Download Done")

try:
	Videos.streams.filter(progressive=False, only_audio=True , abr="128kbps" , type="audio").first().download(output_path="./save")
	# for stream in Videos.streams:
	# 	print(stream)
	Videos.register_on_complete_callback(finish())
except:
	Videos.streams.get_lowest_resolution().download(output_path="./save")
	Videos.register_on_complete_callback(finish())

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