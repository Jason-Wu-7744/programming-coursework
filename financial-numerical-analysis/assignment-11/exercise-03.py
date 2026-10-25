# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd


def PowerMethod_EigenValueVector(A, E):
    n = len(A)
    # 定义初始特征向量
    z0 = np.random.random((n,1))
    lambda0 = 0.9
    lambda1 = 1.0
    i = 0
    while abs(lambda1 - lambda0) > E:
        lambda0 = lambda1
        w = np.dot(A, z0)
        absw = abs(w)
        # np.argmax返回最大值的索引
        i_maxabsw = np.argmax(absw)
        # 标准化特征向量和特征值
        z1 = w/w[i_maxabsw]
        lambda1 = w[0]/z0[0]
        # 一旦选定了k=0，就不能再发生改变
        print("第"+str(i)+"次迭代的特征值为：")
        print(lambda1[0])
        print("第"+str(i)+"次迭代的特征向量为：")
        print(z0)
        i += 1
        z0 = z1
    eigvalue = lambda1
    eigvector = z1
    return eigvalue, eigvector


data = pd.read_csv('Exp11-Python-上机数据_RankSectors.csv')
print(data)

# 先生成所有行业的总集合。用set取出横纵的所有行业再取并集。最后用sorted排序以防最后的方阵不对称。
industry = sorted(set(data['from_sector']) | set(data['to_sector']))
data = data.pivot(index='from_sector', columns='to_sector', values='weight')
print(data)
# 如果只写pivot则不是方阵
data = data.reindex(index=industry, columns=industry)
data = data.fillna(0)
print(data.isnull().sum())
print(data)


eigvalue, eigvector = PowerMethod_EigenValueVector(data, 10**-6)
print(eigvalue)
print(eigvector)

eigvector_dict = {}
for i in range(len(eigvector)):
    eigvector_dict[industry[i]] = eigvector[i, 0]
print(eigvector_dict)

# reverse=True从大到小
# lambda kv: kv[1]表示键值对的值，这里用值来排序
# eigvector_dict.items()把字典里的键和值打包成一个个元组
top10_keys = [k for k, v in sorted(eigvector_dict.items(), key=lambda kv: kv[1], reverse=True)][:10]
print("风险传导网络中影响力排名前十的行业为：\n", top10_keys)