import os

while True:

    # create folder porject

    name_main_folder = input('Enter Your Name Folder \n')

    if not os.path.exists(name_main_folder):
        os.mkdir(name_main_folder)
        
    check_name_other_folder = 'y'

    while check_name_other_folder == 'y':

        check_name_other_folder = input('do you want Make Other Folder (y or n) ? \n')

        if check_name_other_folder == 'y':
            name_other_folder = input('Enter Your Name Folder js \n')
            if not os.path.exists(name_other_folder):
                os.mkdir(name_other_folder)

    os.chdir(name_main_folder)

    print('You Now In ==> ' + name_main_folder )

    check_name_in_main_folder = 'y'

    while check_name_in_main_folder == 'y':

        check_name_in_main_folder = input('do you want Make Other Folder (y or n) ? \n')

        if check_name_in_main_folder == 'y':
            name_other_folder = input('Enter Your Name Folder  \n')
            if not os.path.exists(name_other_folder):
                os.mkdir(name_other_folder)

    ############################################################################################

    # create js folder && file

    check_name_folder_js = input('do you want Folder js With File js (y or n) ? \n')

    if check_name_folder_js == 'y':
        name_folder_js = input('Enter Your Name Folder js \n')
        if not os.path.exists(name_folder_js):
            os.mkdir(name_folder_js)
            os.chdir(name_folder_js)
            open('main.js', 'w+')
            os.chdir('../')

    elif check_name_folder_js == 'n':
        check_name_file_js = input('do you want File js (y or n) ? \n')
        if check_name_file_js == 'y':
            open('main.js', 'w+')
        else:
            print('oky thanks')

    ############################################################################################

    # create html folder && file

    check_name_folder_html = input('do you want Folder html With File html (y or n) ? \n')

    if check_name_folder_html == 'y':
        name_folder_html = input('Enter Your Name Folder html \n')
        if not os.path.exists(name_folder_html):
            os.mkdir(name_folder_html)
            os.chdir(name_folder_html)
            open('index.html', 'w+')
            os.chdir('../')

    elif check_name_folder_html == 'n':
        check_name_file_html = input('do you want File html (y or n) ? \n')
        if check_name_file_html == 'y':
            open('index.html', 'w+')
        else:
            print('oky thanks')

    ############################################################################################

    # create css folder && file

    check_name_folder_css = input('do you want Folder css With File css (y or n) ? \n')

    if check_name_folder_css == 'y':
        name_folder_css = input('Enter Your Name Folder css \n')
        if not os.path.exists(name_folder_css):
            os.mkdir(name_folder_css)
            os.chdir(name_folder_css)
            open('style.css', 'w+')
            os.chdir('../')

    elif check_name_folder_css == 'n':
        check_name_file_css = input('do you want File css (y or n) ? \n')
        if check_name_file_css == 'y':
            open('style.css', 'w+')
        else:
            print('oky thanks')

    ############################################################################################
