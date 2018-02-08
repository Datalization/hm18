class Parent:
    def myMethod(self):
        print('ww')

class Child(Parent):
    def test(self):
        print('yy')

c=Child()
c.myMethod()
c.test()        
