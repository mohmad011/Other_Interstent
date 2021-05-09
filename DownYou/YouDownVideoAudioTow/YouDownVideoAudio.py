from pytube import YouTube
import time
from plyer import notification
Rerun = 'y'

while Rerun != 'n' :
	link = input("Please Inter Your Vedio Url:...\n")
	audioVideo = input("Do You Need (mp4 or mp3) :...\n")
	QualityVideo = input("Plaese Enter The Quality Video (144 or 240 or 360 or 480 or 720 or 1080) :...\n")

	Videos = YouTube(link)

	def finish():
		print( Videos.title +  "\nDownload Done")

	if audioVideo == 'mp4':
		try:
			print("Downloading....")
			if QualityVideo != "144" and QualityVideo != "240" and QualityVideo != "360" and QualityVideo != "480" and QualityVideo != "720" and QualityVideo != "1080":
				Videos.streams.filter(file_extension='mp4',progressive=True,res="360p").order_by('resolution').desc().first().download(output_path="./save")
				Videos.register_on_complete_callback(finish())
				notification.notify(
						title = "Download Done for Video \n" + Videos.title,
						message = "the file is downloaded as Quality 360p",
						timeout = 5
					)
			else:
				Videos.streams.filter(file_extension='mp4',progressive=True,res=QualityVideo + "p").order_by('resolution').desc().first().download(output_path="./save")
				Videos.register_on_complete_callback(finish())
				notification.notify(
							title = "Download Done for Video \n " + Videos.title,
							message = "the file is downloaded as Quality " + QualityVideo,
							timeout = 5
						)
		except:
			print("Downloading....")
			Videos.streams.get_lowest_resolution().download(output_path="./save")
			Videos.register_on_complete_callback(finish())
			notification.notify(
					title = "Download Done for Video " + Videos.title,
					message = "the file is downloaded as Low Quality",
					timeout = 5
				)

	Rerun = input("Do You Want To Re Run Code (y or n) ?....\n")


##########################################################################################

