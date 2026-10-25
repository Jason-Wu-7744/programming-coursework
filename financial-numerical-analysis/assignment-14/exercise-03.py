# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})
plt.rcParams['font.family'] = 'SimHei'

# 梯形法
L = 50
R = 50
E = 10

def I_diff(t, I):
    f = -R/L*I+E/L
    return f

t_list = np.arange(0, 0.0201, 0.0001)

I_trape = [0]
for i in range(len(t_list)-1):
    I_trape.append(0.99995/1.00005*I_trape[i]+0.00002/1.00005)

data = pd.DataFrame({"t": t_list, "I_trape": I_trape})
print(data)

# 龙格-库特法（梯形公式）
h = 0.0001
I_trk = [0]
for i in range(len(t_list)-1):
    I_trk.append(I_trk[i]+h/2*(I_diff(t_list[i], I_trk[i])+I_diff(t_list[i+1], I_trk[i]+h*I_diff(t_list[i], I_trk[i]))))

data['I_trk'] = I_trk
print(data)

# 龙格-库特法（中点公式）
I_mrk = [0]
for i in range(len(t_list)-1):
    a = I_diff(t_list[i], I_mrk[i])
    I_mrk.append(I_mrk[i]+h*I_diff(t_list[i]+h/2, I_mrk[i]+h/2*a))

data['I_mrk'] = I_mrk
print(data)

plt.figure(1, figsize=(16, 9))
plt.plot(data['t'], data['I_trape'])
plt.plot(data['t'], data['I_trk'])
plt.plot(data['t'], data['I_mrk'])
plt.legend(['梯形法', '龙格-库特法（梯形公式）', '龙格-库特法（中点公式）'])
plt.xlabel(r"$t$")
plt.ylabel(r"$I$")
plt.title('homework14_3')
plt.savefig('exercise-03.eps', dpi=300, bbox_inches='tight')
plt.savefig('exercise-03.jpg', dpi=300, bbox_inches='tight')
plt.show()

# 步长 h = 0.0001 太小，三种方法在这么细的步长下截断误差都远远小于绘图精度，于是肉眼看起来“一模一样
# 画出来的其实就是指数曲线最前面的一小段，肉眼看上去就是直线