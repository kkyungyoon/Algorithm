from collections import defaultdict
df = defaultdict(int)
S = input()
for idx, s in enumerate(S):
    for n in range(97, 123):
        if s == chr(n) and s not in df:
            df[s] = idx
            break

df2 = defaultdict(int)
for n in range(97,123):
    df2[chr(n)] = -1

for i in df.keys():
    df2[i] = df[i]

ans = df2.values()
print(*ans)