T = int(input())
for _ in range(T):
    R, S = input().split()
    res = []
    for mun in S:
        last = mun*int(R)
        res.append(last)
    print(''.join(res))