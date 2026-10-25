# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#while循环
chicken_father = 0
chicken_mother = 0
chicken_kid = 0
while chicken_father <= 20:
    chicken_mother = 0
    chicken_kid = 0
    # print(chicken_mother, chicken_kid)
    #一开始没有写上面两行导致输出为空，这是因为鸡孩和妈数值没有重置
    while chicken_mother <= 33:
        chicken_kid = 0
        # 一开始没有写上面一行导致输出为空，这是因为鸡孩数值没有重置
        while chicken_kid <= 100:
            if (5*chicken_father + 3*chicken_mother + chicken_kid/3) == 100 and (chicken_father + chicken_mother + chicken_kid) == 100:
                # print(chicken_father, chicken_mother, chicken_kid)
                print("鸡翁"+str(chicken_father)+"只、鸡母"+str(chicken_mother)+"只、鸡雏"+str(chicken_kid)+"只")
            chicken_kid += 1
        chicken_mother += 1
    chicken_father += 1

#for循环
#考虑到数值重置的问题，用for循环更为合理
for chicken_father in range(0, 21):
    for chicken_mother in range(0, 34):
        for chicken_kid in range(0,101):
            if (5 * chicken_father + 3 * chicken_mother + chicken_kid / 3) == 100 and (chicken_father + chicken_mother + chicken_kid) == 100:
                # print(chicken_father, chicken_mother, chicken_kid)
                print("鸡翁" + str(chicken_father) + "只、鸡母" + str(chicken_mother) + "只、鸡雏" + str(chicken_kid) + "只")
#可以看出，在处理这些需要不断从头开始的嵌套循环时，for比while简便得多

