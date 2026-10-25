# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
i = 1
while i <= 100000:
    if i%7 == 0 and i%11 == 0 and i%13 == 0:
        print(str(i)+"同时能被7、11、13整除")
    i += 1
