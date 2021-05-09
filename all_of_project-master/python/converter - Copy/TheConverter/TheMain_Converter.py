import moviepy.editor as mp
import os

## while True:
    ## current_dir = os.path.dirname(os.path.realpath(__file__))

# ('.mp4', '3gp', 'avi', 'flv', '.h264', 'm4v', 'webm', 'mkv', 'mov', '3g2', 'mpg', 'rm', 'swf', 'vob', 'wmv')
for filename in os.listdir('.'):
    if filename.endswith(('3gp', 'avi', 'flv', '.h264', 'm4v', 'webm', 'mkv', 'mov', '3g2', 'mpg', 'rm', 'swf', 'vob', 'wmv')):
        if not os.path.exists('Videos'):
            os.mkdir('Videos')

        clip = mp.VideoFileClip(os.path.join(filename))
        clip.write_videofile(os.path.join('Videos', filename + '.mp4'))
        print('Videos done')
            
        # clip = mp.VideoFileClip(filename)
        # clip.audio.write_audiofile('Audios' + '/' + filename + '.mp3')
            

