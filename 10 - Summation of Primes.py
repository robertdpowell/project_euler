import math

primes = []
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

for i in range (1, 2000000):
    if is_prime(i):
        primes.append(i)

print (sum(primes))