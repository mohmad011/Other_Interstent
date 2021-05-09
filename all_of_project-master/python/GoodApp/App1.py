from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from os import path
import sys
import pafy
import youtube_dl
import urllib.request
import humanize

class faster_downloader:
    def __init__(self):
        print('welcome in downloader app ... ^_^'.title())
        print('choose number from our collection'.title())
        print('press[1] : download vedio'.title())
        print('press[2] : download playlist'.title())
        self.choices()
           
#########################################################################
    def choices(self):
        while True:
            user_choices = input('enter your number... '.title())
            try:
                user_choices = int(user_choices)
                if user_choices ==  1:
                    self.download_vedio()
                elif user_choices == 2:
                    self.download_playlist()
                else:
                    print('please enter ( 1 or 2  )'.title())
            except:
                print('please enter a valid number'.title())
#########################################################################
    def download_vedio(self):
        video_link = input('enter your link...')
        v = pafy.new(video_link)
        st = v.allstreams
        for s in st:
            size = humanize.naturalsize(s.get_filesize()) ## for return to Magbyte
            data = '{} {} {} {}'.format(s.mediatype , s.extension , s.quality  , size )
            info = []
            print(info.append(data))
        
        for i in info:
            print(range(0 , len(info)+1) ,'=>', i)
        #########################################
        quality = int(input('enter your quality as number ( 0 , 1 , 2 , 3 ,........)'.title()))
        save = input('do you want save this ? ( yes or no)')
        if save == 'yes':
                  file = os.chdir(path)
        else:
                  print('error this is can\'t'.title())
        down = st[quality].download(filepath=file)

#########################################################################
    def download_playlist(self):
                  pass

        
                  
download = faster_downloader()                  
