# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

t = np.arange(0, 2*np.pi+0.1, 0.1)
rho1 = np.abs(np.sin(t)*np.cos(t))
rho2 = np.abs(np.sin(t)*np.cos(2*t))
rho3 = np.abs(np.sin(2*t)*np.cos(t))

# plt.figure(1)
# plt.subplot(2, 1, 1, polar=True)
# plt.polar(t, rho1, 'o-b')
# plt.subplot(2, 2, 3, polar=True)
# plt.polar(t, rho2, 's--r')
# plt.subplot(2, 2, 4, polar=True)
# plt.polar(t, rho3, 'v:k')
#
# plt.savefig('exercise-04.jpg', dpi=600, bbox_inches='tight')
# plt.show()
# #极坐标中若使用subplot需要在subplot中加入polat=True


plt.figure(1)
plt.polar(t, rho1, 'o-b')
plt.savefig('exercise-04_1.jpg', dpi=600, bbox_inches='tight')

plt.figure(2)
plt.polar(t, rho2, 's--r')
plt.savefig('exercise-04_2.jpg', dpi=600, bbox_inches='tight')
plt.figure(3)
plt.polar(t, rho3, 'v:k')
plt.savefig('exercise-04_3.jpg', dpi=600, bbox_inches='tight')
#存在多个画布时savefig只能保存最后一个

plt.show()