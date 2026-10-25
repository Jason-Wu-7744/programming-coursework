# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

g = 9.8
c = 0.27
m = 70

# 第一小题
def equation_v_diff(t, v):
    f = g - (c*v**2)/m
    return f

# 第二小题
# 向前欧拉法
t_list = np.arange(0, 20.1, 0.1)

v_front = [0]
for i in range(len(t_list)-1):
    v_front.append(v_front[i]+0.1*equation_v_diff(t_list[i], v_front[i]))

data = pd.DataFrame({'t': t_list, 'v_front': v_front})
print(data)

# 向后欧拉法
v_back = [0]
for i in range(len(t_list)-1):
    v_back.append((-1+np.sqrt(1+2*c/5/m*(v_back[i]+0.1*g)))*5*m/c)
data['v_back'] = v_back
print(data)

plt.figure(1)
plt.plot(data['t'], data['v_front'])
plt.plot(data['t'], data['v_back'])
plt.legend(['Euler_front', 'Euler_back'])
plt.xlabel(r"$t$")
plt.ylabel(r"$v$")
plt.title('homework14_2')
plt.savefig('exercise-02.eps', dpi=300, bbox_inches='tight')
plt.savefig('exercise-02.jpg', dpi=300, bbox_inches='tight')
plt.show()