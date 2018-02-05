def add (a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
	return a*b
def devide(a, b):
	return a/b

num1 = input ("输入第一个数字")
num2 = input ("输入第二个数字")
num1 = int (num1)
num2 = int (num2)

calculation = input ("输入运算关系")

if calculation == "+" :
    print (add(num1, num2))
if calculation == "-" :
    print (subtract(num1, num2))
if calculation == "*" :
    print (multiply(num1, num2))
if calculation == "/" :
    print (devide(num1, num2))    
