import moviepy.editor as mp
import os

## while True:
    ## current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir('.'):
    if filename.endswith((('.mp3', 'm4a', 'aif', 'cda', 'mid', 'midi', 'mpa', 'ogg', 'wav', 'wma', 'wpl')):
        if not os.path.exists('Audios_Formate'):
            os.mkdir('Audios_Formate')
        my_audio_formate = input('Enter Your Video Formate ( mp3 or webm or m4a or ...)')
        clip = mp.AudioFileClip(os.path.join(filename))
        clip.audio.write_audiofile(os.path.join('Audios_Formate', filename + '.' + my_audio_formate))
        
        print('Audios done')

os.remove(filename)        
        # clip = mp.VideoFileClip(filename)
        # clip.audio.write_audiofile('Audios' + '/' + filename + '.mp3')
            

