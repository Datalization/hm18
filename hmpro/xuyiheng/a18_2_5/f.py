class People:
    name = ''
    age = 0
    __weight = 0#定义私有属性，在类外部无法直接访问
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我今年 %d 岁" %(self.name, self.age))

class Student(People):
    grade = ''
    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("%s 说：我今年 %d 岁了，在读 %d 年级" %(self.name, self.age, self.grade))

s = Student('ken', 10, 40, 3)
s.speak()
