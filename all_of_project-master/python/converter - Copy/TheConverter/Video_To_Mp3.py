import moviepy.editor as mp
import os

## while True:
    ## current_dir = os.path.dirname(os.path.realpath(__file__))

# ('.mp4', '3gp', 'avi', 'flv', '.h264', 'm4v', 'webm', 'mkv', 'mov', '3g2', 'mpg', 'rm', 'swf', 'vob', 'wmv')
for filename in os.listdir('.'):
    if filename.endswith(('mp4', '3gp', 'avi', 'flv', '.h264', 'm4v', 'webm', 'mkv', 'mov', '3g2', 'mpg', 'rm', 'swf', 'vob', 'wmv')):
        if not os.path.exists('Videos_Formate'):
            os.mkdir('Videos_Formate')
        # my_video_formate = input('Enter Your Video Formate ( mp4 or webm) \n')
        clip = mp.VideoFileClip(os.path.join(filename))
        clip.audio.write_audiofile(os.path.join('Videos_Formate', filename + '.' + 'mp3'))
        clip.close()
        
        print('videos done')

        
        # clip = mp.VideoFileClip(filename)
        # clip.audio.write_audiofile('Audios' + '/' + filename + '.mp3')
            

