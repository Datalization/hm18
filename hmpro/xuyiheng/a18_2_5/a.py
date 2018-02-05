#面向过程

std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print('%s, %s' % (std['name'], std['score']))

#面向对象

class Student(object):

    def __init__ (self, name, score):

        self.name = name
        self.score = score

    def print_score(self):
    	 print("asf")
         print(self.name,self.score)
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
