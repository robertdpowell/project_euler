p = 600851475143
n = 2 #our potential factor
while n * n < p: #the largest prime factor will always be smaller than the square root of p
    while p%n == 0:
        p = p / n
    n = n + 1
print (p)
