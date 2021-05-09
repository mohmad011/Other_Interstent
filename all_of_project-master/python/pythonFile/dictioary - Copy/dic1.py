from gtts import gTTS
import os
from pygame import mixer
from tempfile import TemporaryFile

tts = gTTS(u' مرحبا انا اسمي محمد جمال ما اسمك',lang='ar')

mixer.init()

sf = TemporaryFile()

tts.write_to_fp(sf)

sf.seek(0)

mixer.music.load(sf)

mixer.music.play()

# tts.save('name1.mp3')
##os.system("hello.mp3")
input('press to exit.....')
