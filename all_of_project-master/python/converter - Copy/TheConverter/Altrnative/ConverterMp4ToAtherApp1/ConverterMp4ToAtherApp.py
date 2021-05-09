import moviepy.editor as mp
import os

## while True:
    ## current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir('.'):
    if filename.endswith(('.mp4', '3gp', 'avi', 'flv', '.h264', 'm4v', 'webm', 'mkv', 'mov', '3g2', 'mpg', 'rm', 'swf', 'vob', 'wmv')):
        if not os.path.exists('Videos_Formate'):
            os.mkdir('Videos_Formate')
        my_video_formate = input('Enter Your Video Formate ( mp4 or webm or m4v or ...)')
        clip = mp.VideosFileClip(os.path.join(filename))
        clip.video.write_videofile(os.path.join('Videos_Formate', filename + '.' + my_video_formate))
        
        print('videos done')

os.remove(filename)        
        # clip = mp.VideoFileClip(filename)
        # clip.audio.write_audiofile('Audios' + '/' + filename + '.mp3')
            

