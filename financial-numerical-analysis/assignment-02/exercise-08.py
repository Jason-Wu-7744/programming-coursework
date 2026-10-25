# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

def time(i):
    t = 0
    path = np.random.randint(1, 4)
    if path == 1:
        t += 2
    elif path == 2:
        t = 4 + time(i)
    else:
        t = 6 + time(i)
    return t

alltime = 0
for i in range(1, 10001):
    # print("第"+str(i)+"次走到地面消耗的时间为"+str(time(i))+"小时")
    alltime += time(i)
    avgtime = alltime/i
print("可怜的小猫走出山洞的期望时间是"+str(avgtime)+"小时")