std1={'name':'xx','score':'xxx'}
std2={'name':'ww','score':'www'}
def print_score(std):
    print('%s:%s'%(std['name'],std['score']))

class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s'%(self.name,self.score))

if __name__=='__main__':
        bart=Student('bart ss',59)
        lisa=Student('lisa ss',87)
        bart.print_score()
        lisa.print_score()
