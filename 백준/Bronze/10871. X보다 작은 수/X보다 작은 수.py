N, X = map(int, input().split())
A = list(map(int, input().split()))

L = []
for a in A:
  if a < X:
    L.append(a)
print(*L)