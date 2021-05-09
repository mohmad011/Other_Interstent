import os
from moviepy.editor import *
video = VideoFileClip(os.path.join('C:\Users\Mohmad\Documents\New folder',"to","movie.mp4"))
video.audio.write_audiofile(os.path.join("C:\Users\Mohmad\Documents\New folder","to","movie_sound.mp3"))
