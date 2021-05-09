from pytube import YouTube

link = input("Please Inter Your Vedio Url:...\n")

# link = "https://www.youtube.com/watch?v=3W-yNYYHnpQ"

Videos = YouTube(link)

def finish():
	print("Download Done")

try:
	Videos.streams.filter(progressive=True, file_extension='mp4' , res="360p" , type="video").order_by('resolution').desc().first().download(output_path="./save")
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