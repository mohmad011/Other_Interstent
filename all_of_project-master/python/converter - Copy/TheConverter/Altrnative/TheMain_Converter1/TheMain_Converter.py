import moviepy.editor as mp
import os

## while True:
    ## current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir('.'):
    if filename.endswith(('.mp4', '3gp', 'avi', 'flv', '.h264', 'm4v', 'webm', 'mkv', 'mov', '3g2', 'mpg', 'rm', 'swf', 'vob', 'wmv')):
        if not os.path.exists('Audios'):
            os.mkdir('Audios')

        clip = mp.VideoFileClip(os.path.join(filename))
        clip.audio.write_audiofile(os.path.join('Audios', filename + '.mp3'))
        print('Audios done')

os.remove(filename)             
        # clip = mp.VideoFileClip(filename)
        # clip.audio.write_audiofile('Audios' + '/' + filename + '.mp3')
            

