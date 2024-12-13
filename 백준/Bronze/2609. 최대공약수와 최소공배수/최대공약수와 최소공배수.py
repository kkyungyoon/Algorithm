N, M = map(int, input().split())
a, b = N, M

while M != 0:
    N, M = M, N % M
bae = (a * b) // N

print(N)
print(bae)