# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
s = 0
i = 1
while i <= 10**6+1:
    s += i*(1+10**(-6))**(10**6+1-i)
    # print(s)
    i += 1
print(s)

