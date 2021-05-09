print('welcome in the Even-Odd Game')
print('please Enter A Number ... And I Will Tell You if it Even or Odd')
print('if you Wanna Close the Game Enter X ')

while True:
    number = input('Enter A Number ' )
    if number == 'x':
        print('closing the game')
        print('Thanks...')
        break
    try:
        number = int(number)
        if number % 2 == 0:
            print('Even Number')
        else:
            print('Odd Number')
    except ValueError:
        print('Please Enter A Valid Number')
        print('-----------------------------')
