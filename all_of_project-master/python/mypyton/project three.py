print('welcome in multiplication app '.title())
print('please enter the first number and the last number of the multiplication table'.title())
start = int(input('enter the first number of the table: '.title()))
end = int(input('enter the last number of the table: '.title()))
for i in range(start,end+1):
    for x in range(1,13):
        print(i , 'x' ,x , '=' , i * x)
    print('----------------------------')
