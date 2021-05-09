class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b
class powering(calc):
    def power(self):
        return pow(self.a , self.b)

key = 'yes'
while key == 'yes':
    p = powering(int(input('inter first number  ')),int(input('inter second number  ')))
    print('the addtion is  ( {} ) '.format(p.add()))
    print('the muliblication is  ( {} ) '.format(p.mul()))
    print('the powering  is  ( {} ) '.format(p.power()))
    key = input('do you want return the process ?? ( yes or no ) \n')

