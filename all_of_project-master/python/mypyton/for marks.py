class student:
    def __init__(self,name):
        self.name = name
        self.marks = []
        print('welcome {} in the school'.format(name))

    def addmarks(self, mark):
        self.marks.append(mark)

    def avr(self):
        return sum(self.marks)/len(self.marks)
key = 'yes'    
while key == 'yes':
    s1 = student(input('inter your name for add marks '))
    print(s1)
    s1.addmarks(int(input('inter your marks ')))
    s1.addmarks(int(input('inter your marks ')))
    s1.addmarks(int(input('inter your marks ')))
    s1.addmarks(int(input('inter your marks ')))
    s1.addmarks(int(input('inter your marks ')))
    print(s1.avr())
    key = input('do you want return the process ?? ( yes or no )')
