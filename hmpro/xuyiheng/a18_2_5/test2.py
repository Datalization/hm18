num1 = input('输入第一个数字')
num2 = input('输入第二个数字')

num1 = int (num1)
num2 = int (num2)
a = int(0)
b = int(0)
if (num1 > num2):
    a = num1
else:
    a = num2

for i in range (1,a):
    if ((num1 % i == 0) and (num2 % i == 0)):
        b = i

print (b)
