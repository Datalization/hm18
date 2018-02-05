a = input("输入第一个数字")
b = input("输入第二个数字")
a = int(a)
b = int(b)

def greatestcommondivisor(a, b):

   if a > b:
       smaller = b
   else:
       smaller = a

   for i in range(1,smaller+1):
       if((a % i == 0) and (b % i == 0)):
           greatestcommondivisor = i

   return greatestcommondivisor

print(greatestcommondivisor(a,b))
