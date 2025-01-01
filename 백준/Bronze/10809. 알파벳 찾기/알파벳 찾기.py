"""
ord('A') = 65
ord('Z') = 90
ord('a') = 97
ord('z') = 122
알파벳 개수 26개
"""
S = input()
df = dict()
# df = [-1]*(ord('z')-ord('a')+1)
for n in range(97,123):
    df[chr(n)] = -1

for idx, s in enumerate(S):
    if df[s] == -1:
        df[s] = idx
ans = df.values()
print(*ans)