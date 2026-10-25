# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import matplotlib.pyplot as plt
(plt.rcParams.
 update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"}))

plt.figure(1)
plt.pie([15, 60, 25])
plt.legend(['others 15%', 'US 60%', 'EU 25%'], loc='lower right', fontsize=16)
plt.title('Geographical distribution of sales(2025)', fontsize=24)
plt.savefig('1.jpg', dpi=300, bbox_inches='tight')


plt.figure(2)
plt.pie([7, 20, 73])
plt.legend(['others 7%', 'China 20%', 'South East Asia 73%'], loc='lower right', fontsize=16)
plt.title('Distribution of product origins in the US(2025)', fontsize=24)
plt.savefig('2.jpg', dpi=300, bbox_inches='tight')


plt.figure(3)
plt.pie([50, 50])
plt.legend(['China 50%', 'EU 50%'], loc='lower right', fontsize=16)
plt.title('Distribution of product origins in the EU(2025)', fontsize=24)
plt.savefig('3.jpg', dpi=300, bbox_inches='tight')




plt.show()
