import os
converter = os.system('ffmpeg -i movie.mp4 -codec copy test.mp3')

print(converter)
