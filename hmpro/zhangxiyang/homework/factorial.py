a = input("请输入数字")
a = int(a)
def factorial(a):
    x = 1
    for i in range(1,a+1):

        x = x*i
    return x
print(factorial(a))
