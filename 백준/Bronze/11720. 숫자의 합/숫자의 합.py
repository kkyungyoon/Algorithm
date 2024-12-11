N = int(input())
num = list(input())
for idx, n in enumerate(num):
  num[idx] = int(n)
print(sum(num))