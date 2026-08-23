import math

phi = (1+math.sqrt(5))/2
phi_conjugate = (1-math.sqrt(5))/2
answer = 0

for i in range(1, 34):
    ithFibonacci = int((phi ** i - phi_conjugate ** i) / math.sqrt(5))
    if ithFibonacci % 2 == 0:
        answer += ithFibonacci

print(answer)
