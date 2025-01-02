from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# BFS를 위한 큐 초기화 : 큐에는 항상 익은 토마토의 좌표가 들어감
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1 # box에 날짜 입력
            queue.append((nx, ny))

ans = 0
# flag로 푼 경우-------------------------------------------
flag = False

for row in box:
    for tomato in row:
        if tomato == 0: # 토마토가 모두 익지 못 하는 경우
            flag = True
            break
    if flag: # flag가 True면 밖 for문 종료
        break

if flag: # 토마토가 모두 익지 못 하는 경우
    print(-1)
else:
    ans = max(map(max, box)) # 2차원배열
    print(ans-1)