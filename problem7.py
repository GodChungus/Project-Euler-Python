import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0

for i in range(1, 1000000):
    if isPrime(i):
        count += 1
    if count == 10001:
        print(i)
        break
