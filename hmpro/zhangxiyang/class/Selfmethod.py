class site:
    def __init__(self,name,url):
        self.name = name
        self.__url = url

    def __ha(self):
        print("%s:%s"%(self.name,self.__url))

    def ha(self):
        self.__ha()

w = site("emmmm","www.ha.com")
w.ha()
#w.__ha()
