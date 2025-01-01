ans = set()
for _ in range(10):
    n = int(input())
    m = n % 42
    ans.add(m)
print(len(ans))