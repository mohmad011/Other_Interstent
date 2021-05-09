x = 'this program will take several numbers then average them. '.title()

springs = int(input('how many numbers would you like to sum: '.title()))
current_count = 0
sum = 0
while current_count < springs:
    number = float(input('enter a number: '.title()))
    sum = sum + number
    current_count += 1
print('the sum is: '.title() , sum)
print('the avarage is: '.title() , sum / springs)
