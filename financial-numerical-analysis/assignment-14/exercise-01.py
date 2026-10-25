# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

def equation_y(x):
    y = (1+x**2)**(1/3)
    return y

def equation_y_diff(x, y):
    f = 2/3*x*y**(-2)
    return f

x_list = np.arange(0, 1.25, 0.05)

y_real_list = []
for i in x_list:
    y_real_list.append(equation_y(i))
print(y_real_list)

y_sim_list = [1]
for i in range(len(x_list)-1):
    y_sim_list.append(y_sim_list[i]+0.05*equation_y_diff(x_list[i], y_sim_list[i]))
print(y_sim_list)

data = pd.DataFrame({"x": x_list, "y_sim": y_sim_list, "y_real": y_real_list})
print(data)
data['error'] = data['y_real'] - data['y_sim']
data['ratio'] = data['error'].shift(1)/data['error']
print(data)

plt.figure(1)
plt.plot(data['x'], data['y_real'])
plt.plot(data['x'], data['y_sim'])
plt.legend(['real', 'sim'])
plt.title('homework14_1')
plt.savefig('homework14_1.jpg', dpi=300, bbox_inches='tight')
plt.show()

# 误差先扩大再缩小