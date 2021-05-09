class Game:
    ## Constractor for the main game
    def __init__(self):
        print('welcome in full game ... ^_^'.title())
        print('choose your game from our collection'.title())
        print('press[1] : play Even-Odd game'.title())
        print('press[2] : play sum-avarege game'.title())
        print('press[3] : play Multiplication game'.title())
        self.choices()


########################################################################################

    ## Available Choices
    def choices(self):
        while True:
            user_choices = input('enter your game '.title())
            try:
                user_choices = int(user_choices)
                if user_choices ==  1:
                    self.Even_Odd_Game()
                elif user_choices == 2:
                    self.Sum_Avarege_Game()
                elif user_choices == 3:
                    self.Multiplication_Game()
                else:
                    print('please enter between 1 or 2 or 3 '.title())
            except:
                print('please enter a valid number'.title())

                
########################################################################################
                
    ## Even-Odd Game Code
    def Even_Odd_Game(self):
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

                
########################################################################################

    ## Sum-Avarege-Game Code
    def Sum_Avarege_Game(self):
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
        
########################################################################################
        
    ## Multiplication-Game Code
    def Multiplication_Game(self):
        print('welcome in multiplication app '.title())
        print('please enter the first number and the last number of the multiplication table'.title())
        start = int(input('enter the first number of the table: '.title()))
        end = int(input('enter the last number of the table: '.title()))
        for i in range(start,end+1):
            for x in range(1,13):
                print(i , 'x' ,x , '=' , i * x)
            print('----------------------------')

            
# Create Object from the class

game = Game()

# creat class
# methods - pass
# creat object from the class
# copy projects
# Add Code constractor
# creat choices method
# handling exception ( charachter , 1 2 3 )
# connect methoda ---- choices
