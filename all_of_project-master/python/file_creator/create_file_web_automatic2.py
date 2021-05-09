import os

# create folder porject

name_folder = input('Enter Your Name Folder \n')

if not os.path.exists(name_folder):
    os.mkdir(name_folder)
    os.chdir(name_folder)

############################################################################################

# create js folder && file

    open('main.js', 'w+')

############################################################################################

# create html folder && file

    open('main.html', 'w+')

############################################################################################

# create css folder && file

    open('main.css', 'w+')

############################################################################################

