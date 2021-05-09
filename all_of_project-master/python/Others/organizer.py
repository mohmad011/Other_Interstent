import os
import shutil

# current_dir = os.path.dirname(os.path.realpath(__file__))

print('welcome in organization files script - happy clean folder')

for filename in os.listdir('.'):

    # orgnize Audio into Audios folder
    try:
        if filename.endswith(('.mp3', 'm4a', 'aif', 'cda', 'mid', 'midi', 'mpa', 'ogg', 'wav', 'wma', 'wpl')):
            if not os.path.exists('Audios'):
                os.mkdir('Audios')
            shutil.copy(filename, 'Audios')
            os.remove(filename)
            print('Audios done')
    except Exception :
            print('error')


    # orgnize videos into videos folder
    try:
        if filename.endswith(('.mp4', '3gp', 'avi', 'flv', '.h264', 'm4v', 'webm', 'mkv', 'mov', '3g2', 'mpg', 'rm', 'swf', 'vob', 'wmv')):
            if not os.path.exists('videos'):
                os.mkdir('videos')
            shutil.copy(filename, 'videos')
            os.remove(filename)
            print('videos done')
    except Exception :
            print('error')

    # orgnize images into images folder
    try:
        if filename.endswith(('.png', 'jpg', 'jpeg', 'gif', 'tif', 'tga', 'rem', 'ico', 'tiff', 'bmp', 'ai', 'psd', 'svg')):
            if not os.path.exists('images'):
                os.mkdir('images')
            shutil.copy(filename, 'images')
            os.remove(filename)
            print('images done')
    except Exception :
            print('error')

    # orgnize [Compressed file] into Compressed_file folder
    try:
        if filename.endswith(('.zip', 'rar', 'tar', 'tgz', 'bz2', 'torrent', 'zipx', '7z', 'ace', 'gtar', 'gz', 'arj', 'deb', 'pkg', 'rpm', 'tar.gz', 'z')):
            if not os.path.exists('Compressed_file'):
                os.mkdir('Compressed_file')
            shutil.copy(filename, 'Compressed_file')
            os.remove(filename)
            print('Compressed_file done')
    except Exception :
            print('error')

    # orgnize [Disc and media] into Disc_media folder
    try:
        if filename.endswith(('.bin', 'dmg', 'iso', 'toast', 'vcd')):
            if not os.path.exists('Disc_media'):
                os.mkdir('Disc_media')
            shutil.copy(filename, 'Disc_media')
            os.remove(filename)
            print('Disc_media done')
    except Exception :
            print('error')

    # orgnize [Data and database] into Data_database folder
    try:
        if filename.endswith(('.csv', 'dat', 'db', 'dbf', 'log', 'mdb', 'sav', 'sql')):
            if not os.path.exists('Data_database'):
                os.mkdir('Data_database')
            shutil.copy(filename, 'Data_database')
            os.remove(filename)
            print('Data_database done')
    except Exception :
        print('error')

    # orgnize [Presentation file] into Presentation_file folder
    try:
        if filename.endswith(('.key', 'odp', 'pps', 'ppt', 'pptx')):
            if not os.path.exists('Presentation_file'):
                os.mkdir('Presentation_file')
            shutil.copy(filename, 'Presentation_file')
            os.remove(filename)
            print('Presentation_file done')
    except Exception :
        print('error')


    # orgnize [Spreadsheet file] into Spreadsheet_file folder
    try:
        if filename.endswith(('.ods', 'xls', 'xlsm', 'xlsx')):
            if not os.path.exists('Spreadsheet_file'):
                os.mkdir('Spreadsheet_file')
            shutil.copy(filename, 'Spreadsheet_file')
            os.remove(filename)
            print('Spreadsheet_file done')
    except Exception :
        print('error')

    # orgnize texts into texts folder
    try:
        if filename.endswith(('.url', 'cbr', 'cbz', 'xml', 'cpp', 'txt', 'c', 'hpp', 'diz', 'log', 'csv')):
            if not os.path.exists('texts'):
                os.mkdir('texts')
            shutil.copy(filename, 'texts')
            os.remove(filename)
            print('texts done')
    except Exception :
        print('error')

    # orgnize [Word processor and text file] into Word_text folder

    try:
        if filename.endswith(('.doc', 'docx', 'odt', 'pdf', 'rtf', 'tex', 'txt', 'wpd', 'docm', 'xlsb', 'dot', 'ps', 'dotm', 'dotx')):
            if not os.path.exists('Word_text'):
                os.mkdir('Word_text')
            shutil.copy(filename, 'Word_text')
            os.remove(filename)
            print('Word_text done')
    except Exception :
            print('error')


    # orgnize code into codes folder
    try:
        if filename.endswith(('.html', 'css', 'js')):
            if not os.path.exists('codes'):
                os.mkdir('codes')
            shutil.copy(filename, 'codes')
            os.remove(filename)
            print('codes done')
    except Exception :
            print('error')


    # orgnize apps into apps folder
    try:
        if filename.endswith(('.dmg', 'exe', 'msi')):
            if not os.path.exists('Programs'):
                os.mkdir('Programs')
            shutil.copy(filename, 'Programs')
            os.remove(filename)
            print('Programs done')
    except Exception :
        print('error')

print('done organizinf the folder')
