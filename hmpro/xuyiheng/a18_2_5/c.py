class Test:
    def prt(self):
        print(self)#打印内存地址
        print(self.__class__)#打印类名
t = Test()
t.prt()
