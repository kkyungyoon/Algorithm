L = int(input())
str = input()
r = 31
M = 1234567891

ans = 0
for l in range(L):
  char = ord(str[l]) - ord('a') + 1
  ans += char * (r ** l)
  ans = ans % M

print(ans)