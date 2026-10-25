# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import scipy as sp

#第一小题
def binomial_pmf(n, p, k):
    comb = sp.special.comb(n, k, exact=True)
    pmf = comb*(p**k)*((1-p)**(n-k))
    return pmf
# print(binomial_pmf(4, 0.5, 2))
def binomial_stats(n, p, k=1):
    e = n*p
    d = n*p*(1-p)
    return e, d
expected_value, variance = binomial_stats(10000, 0.06)
print("保险理赔人数变量的期望值：", expected_value, "\n保险理赔人数变量的标准差：", variance**(1/2))

#第二小题
binomial_samples = np.random.binomial(10000, 0.06, 100)
binomial_samples_mean = np.mean(binomial_samples)
binomial_samples_std = np.std(binomial_samples)
print(binomial_samples_mean, binomial_samples_std)
if binomial_samples_mean <= expected_value*1.1 or binomial_samples_mean >= expected_value*0.9:
    print("抽样结果的平均值与该变量期望值无显著差异")
else:
    print("抽样结果的平均值与该变量期望值有显著差异")
if binomial_samples_std <= variance**(1/2)*1.2 or binomial_samples_std >= variance**(1/2)*0.8:
    print("抽样结果的标准差与该变量标准差无显著差异")
else:
    print("抽样结果的标准差与该变量标准差有显著差异")
#比较结果可能有更加精确的算法，有待后续的学习

#第三小题
def geometric_pmf(p, k):
    return (1-p)**(1-k)*p
def geometric_stats(p, k=1):
    return 1/p, (1-p)/(p**2)
expected_value, variance = geometric_stats(0.005)
print("保单从生效到触发理赔条件所经历的时间长度变量的期望值为", expected_value, "标准差为", variance**(1/2))

#第四小题
geometric_samples = np.random.geometric(0.005, 200)
geometric_samples_mean = np.mean(geometric_samples)
geometric_samples_std = np.std(geometric_samples)
print(geometric_samples_mean, geometric_samples_std)
if geometric_samples_mean <= expected_value*1.1 or geometric_samples_mean >= expected_value*0.9:
    print("抽样结果的平均值与该变量期望值无显著差异")
else:
    print("抽样结果的平均值与该变量期望值有显著差异")
if geometric_samples_std <= variance**(1/2)*1.2 or geometric_samples_std >= variance**(1/2)*0.8:
    print("抽样结果的标准差与该变量标准差无显著差异")
else:
    print("抽样结果的标准差与该变量标准差有显著差异")