num = input('输入第一个数字')

num = int (num)
ans = int (1)

for i in range (1,num):
    ans = ans * i

print (ans)
