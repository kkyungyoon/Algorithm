max = 0
ans_idx = 0
idx = 0
for _ in range(9):
  idx += 1
  N = int(input())
  if N > max:
    max = N
    ans_idx = idx
print(max)
print(ans_idx)