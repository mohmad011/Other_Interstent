class animal:
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print('{} is eat {}'.format(name,food))

class dog(animal):
    def fetch(self , thing):
        print('{} get the {}'.format(name , thing))

class cat(animal):
    def cat_eat(self):
        print('{} is eating food  '.format(name))
