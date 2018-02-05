class Parent:

    def myMethod(self):
        print("Helloworld")

class Child(Parent):

    def test(self):
        print("ha")

c = Child()
c.myMethod()
c.test()
