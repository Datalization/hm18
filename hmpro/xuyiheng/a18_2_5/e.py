class Parent:#定义父类
    def myMethod(self):
        print('调用父类的方法')

class Child(Parent): #调用子类
    def test(self):
        print('调用子类的方法')

c = Child()#子类实例
c.myMethod()#子类调用(!!!调用用'c.'而不是'c=')
c.test()
