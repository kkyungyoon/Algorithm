memo = {}
def fibonacci(n):
    global memo
    if n in memo:  # 이미 계산된 값이 있으면 반환
        return memo[n]
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        fibo_1 = fibonacci(n-1)
        fibo_2 = fibonacci(n-2)
        memo[n] = [fibo_1[0] + fibo_2[0], fibo_1[1] + fibo_2[1]]
        return memo[n]

import sys
input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    print(*fibonacci(N))