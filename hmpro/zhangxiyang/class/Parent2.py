class People:

    name = ""
    age = 5
    __weight = 0
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speak(self):
        print("%s说：我%d岁。"%(self.name,self.age))

class Student(People):

    name = ""
    score= 5

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print ("he")
        print('%s %s' %(self.name, self.score))

if __name__ == '__main__':

    lily = Student("Lily Ha",79)
    lily.print_score()
    lily = People("Lily Ha",5,0)
    lily.speak()
    # print(lily.__weight)
