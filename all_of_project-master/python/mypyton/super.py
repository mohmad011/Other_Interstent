class animal:
    def __init__(self , name):
        self.name = name

class Dog(animal):
    def __init__(self , name):
        super(Dog , self).__init__(name)
        self.food = 'meet'
x = Dog('misho')
print(x.food)
x.food = 'fish'
print(x.food)
