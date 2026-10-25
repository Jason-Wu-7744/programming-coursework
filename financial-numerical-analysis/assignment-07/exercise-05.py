# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

data = pd.read_excel('Exp07-Python-实验数据-轻松筹项目数据.xlsx')
print(data)

n = len(data['筹款金额'])

ln_Mt = data['筹款金额']
ln_Sh = data['项目分享次数']
Qn = data['证明人数']
Qt = data['项目描述长度']
Pa = data['患者年龄']

variable = [ln_Mt, ln_Sh, Qn, Qt, Pa]

variable_sum = []
for a in variable:
    sum = 0
    for b in range(len(ln_Mt)):
        sum += a[b]
    variable_sum.append(sum)
print(variable_sum)

sum_yy = 0
sum_x1x1 = 0
sum_x2x2 = 0
sum_x3x3 = 0
sum_x4x4 = 0
variable_sqr_sum = [sum_yy, sum_x1x1, sum_x2x2, sum_x3x3, sum_x4x4]
for a in range(len(variable)):
    for b in range(len(variable[a])):
        variable_sqr_sum[a] += variable[a][b]**2
print(variable_sqr_sum)

sum_yx1 = 0
sum_yx2 = 0
sum_yx3 = 0
sum_yx4 = 0
sum_x1x2 = 0
sum_x1x3 = 0
sum_x1x4 = 0
sum_x2x3 = 0
sum_x2x4 = 0
sum_x3x4 = 0
variable_inter_sum = [sum_yx1, sum_yx2, sum_yx3, sum_yx4, sum_x1x2, sum_x1x3, sum_x1x4, sum_x2x3, sum_x2x4, sum_x3x4]
variable_inter_sum_index = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

for a in range(len(variable_inter_sum)):
    for b in range(len(ln_Mt)):
        variable_inter_sum += variable[variable_inter_sum_index[a][0]][b]*variable[variable_inter_sum_index[a][1]][b]
print(variable_inter_sum)

A = np.array([[n, variable_sum[1], variable_sum[2], variable_sum[3], variable_sum[4]],
              [variable_sum[1], variable_sqr_sum[1], variable_inter_sum[4], variable_inter_sum[5], variable_inter_sum[6]],
              [variable_sum[2], variable_inter_sum[4], variable_sqr_sum[2], variable_inter_sum[7], variable_inter_sum[8]],
              [variable_sum[3], variable_inter_sum[5], variable_inter_sum[7], variable_sqr_sum[3], variable_inter_sum[9]],
              [variable_sum[4], variable_inter_sum[6], variable_inter_sum[8], variable_inter_sum[9], variable_sqr_sum[4]]
              ])
b = np.array([[variable_sum[0]],
              [variable_inter_sum[0]],
              [variable_inter_sum[1]],
              [variable_inter_sum[2]],
              [variable_inter_sum[3]]
              ])

x = np.dot(np.linalg.inv(A), b)
print(x)

print("回归结果为：")
print("ln_Mt =", x[0, 0], "+", x[1, 0],"*ln_Sh +", x[2, 0],"*Qn +", x[3, 0],"*Qt +", x[4, 0],"*Pa")

# 这个算法依旧使用了原始的矩阵相乘，由于自变量变多已经变得有些复杂。算法优化有待后续的学习。
# 通过回归结果可以看出：
# 项目分享次数每增加1%，筹款金额就平均增加47.6%
# 证明人数每增加一人，筹款金额就平均增加14.4%
# 项目描述长度每增加一单位，筹款金额就平均增加38.6%
# 患者年龄每增加一岁，筹款金额就平均增加14.4%
# 可以看出，想要增加筹款金额，增加项目分享次数和项目描述长度是最有效的。
