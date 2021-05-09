class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b

key = 'yes'
while key == 'yes':
    
    c1 = calc(int(input('inter first number  ')),int(input('inter second number  ')))
    num1 = c1.add()
    num2 = c1.mul()
    print('the sum numbers is {}'.format(num1))
    print('the mul numbers is {}'.format(num2))
    key = input('do you want return the process ?? ( yes or no ) \n')
