N = list(map(int, input().split()))
sum = 0
for n in N:
  sum += n**2
print(sum % 10)