import os
from moviepy.editor import *

key = 'y'
while key == 'y':
    array = []
    vedio_adding = input('Enter The Name Video.... \n' )
    array.append(vedio_adding)
    key = input('do you wont to repet this peosess ?? yes on no \n ').lower()
if key != 'y':
    for v in array:
        video = VideoFileClip(os.path.join(v + '.' + 'mp4'))
        video.audio.write_audiofile(os.path.join(v + 'audio' + '.' + 'mp3'))
else:
    print('errore')
