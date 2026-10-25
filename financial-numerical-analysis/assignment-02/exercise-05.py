# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
s = 0
i = 1
while i <= 64:
    s += 2**(i-1)
    # print(s)
    i += 1
volume = s/1.4/100000000
print("国王共要给达依尔"+str(volume)+"立方米小麦")
