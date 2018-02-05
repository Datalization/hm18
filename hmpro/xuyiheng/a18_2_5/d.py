class people:
    name = ''
    age = 0
    __weight = 0#定义私有属性，在类外部无法直接访问
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我今年 %d 岁" %（self.name, self.age))

p = pelple('runoob', 10, 30)
p.speak()
