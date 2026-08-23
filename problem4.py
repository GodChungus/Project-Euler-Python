def isPalindrome(n):
    return str(n) == str(n)[::-1]


answer = 0
for i in range(1000):
    for j in range(1000):
        if isPalindrome(i*j) and i*j>answer:
            answer = i*j

print(answer)
