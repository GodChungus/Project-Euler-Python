def sumOfSquares(n):
    answer = 0
    for i in range(n+1):
        answer += i*i
    return answer

def squareOfSum(n):
    answer = 0
    for i in range(n+1):
        answer += i
    return answer**2


print(squareOfSum(100)-sumOfSquares(100))
