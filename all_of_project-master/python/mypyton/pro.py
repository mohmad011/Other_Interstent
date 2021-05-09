print('welcome in the Even-Odd Game')
print('please Enter A Number ... And I Will Tell You if it Even or Odd')
print('if you Wanna Close the Game Enter X')

while True:
    num = input('Enter the number ')
    if num == 'x':
        print('closing the game')
        print('Thanks....')
        break
    try:
        num = int(num)
        if num % 2 == 0:
            print('Even Number')
        else:
            print('odd number')
    except ValueError:
        print('Please Enter A Valid Number')
        print('-------------------------')
