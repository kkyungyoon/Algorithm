T = int(input())
for _ in range(T):
    munja = input()
    cnt = 0
    ans = []
    for m in munja:
        if m == 'O':
            cnt += 1
            ans.append(cnt)
        elif m == 'X':
            cnt = 0
    print(sum(ans))        