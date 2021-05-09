class a:
    def dothing(self):
        print('i am in A ' )

class b(a):
    pass

class c:
    def dothing(self):
        print('i am in C ' )

class d(b, c):
    pass

so = d()
so.dothing()

print(d.mro()) ## mro => method reslution order 
