# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import scipy as sp

#第一小题
def gamma_pdf(x, k, theta):
    if x <= 0 or k <= 0 or theta <= 0:
        return "输入值不符要求"
    else:
        return (x**(k-1)*np.e**(-x/theta))/(theta**k*sp.special.gamma(k))
def gamma_stats(k, theta):
    return k*theta, k**(1/2)*theta
print(gamma_pdf(1, 2, 3), gamma_stats(2, 3))

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1 or alpha <= 0 or beta <= 0:
        return "输入值不符要求"
    else:
        return (x**(alpha-1)*(1-x)**(beta-1))/(sp.special.beta(alpha, beta))
def beta_stats(alpha, beta):
    return alpha/(alpha+beta), np.sqrt(alpha*beta/(alpha+beta)**2*(alpha+beta+1))
print(beta_pdf(0.5, 2, 2), beta_stats(2, 2))

#第二小题
arr = np.array(pd.read_excel("exercise-22_1.xlsx"))
# print(arr)
year = arr[:, 0]
arr = np.delete(arr, 0, 1)
arr = arr.astype(float)
# print(arr, arr.dtype)
arr_default = arr[:, 0]
arr_recovery = arr[:, 1]
print("违约率数组为：\n", arr_default)
print("回收率数组为：\n", arr_recovery)

arr_default_amount = 12000000000*arr_default
arr_default_amount_mean = np.mean(arr_default_amount)
arr_default_amount_std = np.std(arr_default_amount)
print("违约金额的均值为", arr_default_amount_mean, "\n违约金额的标准差为", arr_default_amount_std )

arr_recovery_mean = np.mean(arr_recovery)
arr_recovery_std = np.std(arr_recovery)
print("回收率的均值为", arr_recovery_mean, "\n回收率的标准差为", arr_recovery_std)

#第三小题
#通过已知的样本均值标准差倒算参数
#本小题中形状参数为k，尺度参数为theta以和下一小题区分
theta = arr_default_amount_std**2/arr_default_amount_mean
k = arr_default_amount_mean/theta
print(k, theta)

theta_examples = np.random.gamma(k, theta, 100000)
theta_examples_mean = np.mean(theta_examples)
theta_examples_std = np.std(theta_examples)
print("债券违约金额随机抽样结果的均值为", theta_examples_mean, "标准差为", theta_examples_std)

#第四小题
u = arr_recovery_mean
var = arr_recovery_std**2
alpha_plus_beta = (u*(1-u)/var) - 1
alpha = u*alpha_plus_beta
beta = (1 - u)*alpha_plus_beta
beta_samples = np.random.beta(alpha, beta, 100000)
beta_samples_mean = np.mean(beta_samples)
beta_samples_std = np.std(beta_samples)
print("债券违约的回收率随机抽样结果的均值为", beta_samples_mean, "标准差为", beta_samples_std)