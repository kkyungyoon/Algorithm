N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key= lambda x: (x[1], x[0]))
cnt = 0
last_end = 0
for start, end in meetings:
    if start >= last_end: # 겹치지 않음
        cnt += 1
        last_end = end
print(cnt)