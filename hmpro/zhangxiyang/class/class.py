class student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))
if __name__  == "main":
    bart = student('Bart Li',58)
    lily = student("Lily Ha",79)
    print_score(bart)
    print_score(lily) 
