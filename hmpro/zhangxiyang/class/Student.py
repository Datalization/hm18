class Student(object):

    name = ""
    score= 5

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print ("he")
        print('%s %s' %(self.name, self.score))

if __name__ == '__main__':

    bart = Student('Bart Li',58)
    lily = Student("Lily Ha",79)
    bart.print_score()
    lily.print_score()
