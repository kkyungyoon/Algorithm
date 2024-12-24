"""
누적합 : 리스트의 특정 구간 합을 빠르게 계산할 수 있도록 미리 값을 계산해 저장하는 방식
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
num_list = list(map(int, input().strip().split()))

# 누적 합 계산
sum = [0] * (N + 1) # sum[1 - 1] 때문에
for i in range(1, N + 1):
    sum[i] = sum[i - 1] + num_list[i - 1]

for _ in range(M):
    a, b = map(int, input().strip().split())
    print(sum[b] - sum[a-1])