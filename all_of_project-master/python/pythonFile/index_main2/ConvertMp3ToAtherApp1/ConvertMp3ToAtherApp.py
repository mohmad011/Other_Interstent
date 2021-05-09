import moviepy.editor as mp

while True:
    NameAudio = input('Enter The Name Audio.... \n' )
    NameFormatAudio = input('Enter The Name Format Audio (mp3 or m4a or....) \n')
    NameFileConverted = input('Enter The Name Audio Converted.... \n')
    NameFormat = input('Enter The Name Format  (mp3 or m4a or....) \n')
    NameFileAudio = input('Enter The Name File Audio.... \n' )
    NameFileSave = input('Enter The Name File Save.... \n' )
    clip = mp.AudioFileClip( NameFileAudio + '/' + NameAudio + '.' + NameFormatAudio)
    clip.write_audiofile( NameFileSave + '/' + NameFileConverted + '.' + NameFormat)
