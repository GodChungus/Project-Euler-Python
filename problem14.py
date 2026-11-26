# Program could be much faster if we implemented some caching method to store past counts.
# For example, 5 --> 16 --> 8 --> 4 --> 2 --> 1
# If we have 20 --> 10 --> 5, the value for 5 is already stored in the cache, so we can just use that again instead of
# re-calculating for 5. Could save a lot of time for much larger numbers.


def count_collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count+1


answer = 1
max_length = 0
for i in range(1, 1000000):
    if count_collatz(i) > max_length:
        max_length = count_collatz(i)
        answer = i
print(answer)
