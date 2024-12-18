import sys
input = sys.stdin.readline

M = int(input().strip())
# 메모리 초과
# command = [input().strip().split() for _ in range(M)]
S = set()

for _ in range(M):
    c = input().strip().split()
    cmd = c[0]
    # num = int(c[1])

    if cmd == 'add':
        # if c[1] not in S:
        S.add(int(c[1]))
    elif cmd == 'remove':
        # if c[1] in S:
        S.discard(int(c[1]))
    elif cmd == 'check':
        print(0 if int(c[1]) not in S else 1)
    elif cmd == 'toggle':
        S.remove(int(c[1])) if int(c[1]) in S else S.add(int(c[1]))
    elif cmd == 'all':
        S = set(range(1, 21))
    elif cmd == 'empty':
        S.clear()