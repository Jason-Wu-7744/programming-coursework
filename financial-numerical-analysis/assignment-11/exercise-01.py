# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

A = np.array([[3, -4, 3],
              [-4, 6, 3],
              [3, 10, 1]])

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

eigvalue, eigvector = PowerMethod_EigenValueVector(A, 10**-6)
print("特征值为：\n", eigvalue[0])
print("特征向量为：\n", eigvector)