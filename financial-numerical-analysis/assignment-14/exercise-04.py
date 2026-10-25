# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})
plt.rcParams['font.family'] = 'SimHei'

r = 0.0325/12
L = 1000000
# u表示贷款余额，也就是剩余的本金

# 等额本金
def equal_principal_u_diff(t, u):
    f = -L/360
    return f

t_list = np.arange(0, 361, 1)

equal_principal_u = [L]
for i in range(len(t_list)-1):
    equal_principal_u.append(equal_principal_u[i]+1*equal_principal_u_diff(t_list[i], equal_principal_u[i]))

data = pd.DataFrame({"t": t_list, "equal_principal_u": equal_principal_u})
print(data)

# 等额本息
pi = L*r*(1+r)**360/((1+r)**360-1)
print(pi)
def equal_pi_u_diff(t, u):
    f = r*u-pi
    return f
# 每月还的本息先冲抵贷款余额（剩余本金）产生的利息，再减少贷款余额
# 先还利息，再还本金
equal_pi_u = [L]
for i in range(len(t_list)-1):
    equal_pi_u.append(equal_pi_u[i]+1*equal_pi_u_diff(t_list[i], equal_pi_u[i]))

data['equal_pi_u'] = equal_pi_u
print(data)

plt.figure(1, figsize=(16, 9))
plt.plot(data['t'], data['equal_principal_u'])
plt.plot(data['t'], data['equal_pi_u'])
plt.legend(['等额本金', '等额本息'])
plt.xlabel(r"$t$")
plt.ylabel("贷款余额")
plt.title("homework14_4")
plt.savefig('exercise-04.eps', dpi=300, bbox_inches='tight')
plt.savefig('exercise-04.jpg', dpi=300, bbox_inches='tight')
plt.show()
