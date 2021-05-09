import os

# create folder porject

name_folder = input('Enter Your Name Folder \n')

if not os.path.exists(name_folder):
    os.mkdir(name_folder)
    os.chdir(name_folder)

############################################################################################

# create js folder && file

name_folder_js = 'js'
if not os.path.exists(name_folder_js):
    os.mkdir(name_folder_js)
    os.chdir(name_folder_js)
    open('main.js', 'w+')
    os.chdir('../')

############################################################################################

# create html folder && file

    open('main.html', 'w+')

############################################################################################

# create css folder && file

name_folder_js = 'css'
if not os.path.exists(name_folder_js):
    os.mkdir(name_folder_js)
    os.chdir(name_folder_js)
    open('main.css', 'w+')
    os.chdir('../')

############################################################################################

# create images folder

name_folder_js = 'images'
if not os.path.exists(name_folder_js):
    os.mkdir(name_folder_js)

############################################################################################

# create fonts folder

name_folder_js = 'fonts'
if not os.path.exists(name_folder_js):
    os.mkdir(name_folder_js)

############################################################################################
