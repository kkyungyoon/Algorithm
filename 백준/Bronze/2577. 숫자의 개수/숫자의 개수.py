A = int(input())
B = int(input())
C = int(input())
total = A*B*C
str_list = list(str(total))
int_list = [int(st) for st in str_list]
int_list.sort()
from collections import defaultdict
di = defaultdict(int) # 초기화
for i in int_list:
    di[i] += 1
for j in range(0, 10):
    if di[j]:
        print(di[j])
    else:
        print(0)