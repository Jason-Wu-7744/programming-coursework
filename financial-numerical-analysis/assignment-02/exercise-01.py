# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#for循环
s = 0
for i in range(1, 51, 1):
    s += i**3/(i*(i+2))
    # print(i, s)
print("for循环结果为"+str(s))

#while循环
i = 1
s = 0
while i <= 50:
    s += i ** 3 / (i * (i + 2))
    i += 1
    # print(i, s)
print("while循环结果为"+str(s))


#不使用循环
summation = sum((i ** 3 / (i * (i + 2))) for i in range(1, 51))
print("不使用循环结果为"+str(summation))
#这个方法仍然带有一定的循环元素，可能有更加简便的算法

