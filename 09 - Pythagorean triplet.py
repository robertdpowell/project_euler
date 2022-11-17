def findpy (a,b,c):
    if (a ** 2) + (b ** 2) == (c ** 2):
        if a < b < c:
            return(a * b * c)


for i in range (1, 400):
    for j in range (1, 400):
        k = (1000 - j) - i
        if (findpy(i, j, k)):
            print (findpy(i, j, k))

