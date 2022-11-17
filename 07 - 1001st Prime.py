import math

def is_prime(n):
    if n < 2:
        return False # can't be even
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0: # can't be divisible by any number other than itself and 1
            return False
    return True


seen = 0
n = 1
while seen < 10001: #do this until we reach 10001
    n += 1 #start at 1 and increment by 1 every time
    if is_prime(n): #if we get a prime number
        seen += 1

print(n)


print (is_prime(19))


