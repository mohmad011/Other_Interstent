import subprocess
command = "ffmpeg -i C:/Users/Mohmad/Documents/New folder/move.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
print(subprocess.call(command, shell=True))
