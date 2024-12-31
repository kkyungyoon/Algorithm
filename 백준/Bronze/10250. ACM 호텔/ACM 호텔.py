T = int(input())
res = []
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = (N-1) % H + 1
    room = (N-1) // H + 1
    res.append(f'{floor}{room:02}')
print(*res, sep='\n')