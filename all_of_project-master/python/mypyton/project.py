key = 'yes'
users = []
password = []
while key == 'yes':
    acount = input('do you have an acount ?? yes or no \n' ).lower()
    if acount == 'yes':
        print('please login ... ')
        login_user = input(' please inter your username \n').lower()
        login_pass = input(' please inter your password \n').lower()
        if (login_user in users) and (login_pass in password) :
            print('success')
        else:
            print('rong in password or username')
    elif acount == 'no':
        ofer = input('do you wont register with us ?? yes or no \n').lower()
        if ofer == 'yes':
            regist_user = input('please inter your username \n' ).lower()
            regist_pass = input('please inter your password \n' ).lower()
            if (regist_user in users) or (regist_pass in password) :
                print('error password or username is alredy find ' )
            else:
                users.append(regist_user)
                password.append(regist_pass)
                print('Congratulations you is Register now ')
        else:
            print('Thanks for visit us ' )
    else:
        print('I do not understand ' )
    key = input('do you wont to repet this peosess ?? yes on no \n ').lower()
