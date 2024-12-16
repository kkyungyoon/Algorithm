N = int(input())
M = []
for _ in range(N):
    # x, y를 한번에 받아서 append하면 안 됨
    x, y = map(int, input().split())
    # point = list(map(int, input().split()))
    M.append([x, y])
M.sort(key= lambda x: (x[0], x[1]))
for m in M:
    print(*m)