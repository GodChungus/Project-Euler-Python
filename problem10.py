import math

def isPrime(n):
    if(n<2): return False
    if(n==2): return True
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True


answer = 0
for i in range(3, 2000000, 2):
    if(isPrime(i)):
        answer += i
print(answer+2)
