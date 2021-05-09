class myclass:
    def student_info(self,name,age):
        self.name = name
        self.age = age
        print('i am {} and my age is {}'.format(name,age))
    def __init__(self):
        print('you are welcome')
x = myclass()
x.student_info('mohmad',22)
x.student_info('ali',21)
