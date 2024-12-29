"""
DFS(깊이 우선 탐색) : 한 방향으로 깊게 탐색하고 더 탐색할 곳이 없으면 직전에 방문했던 노드로 되돌아가는 방식 - LIFO - 스택사용
BFS(너비 우선 탐색) : 현재 노드와 인접한 노드들을 모두 탐색한 후, 다음 깊이로 넘어가는 방식 - FIFO - 큐
"""
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    visited = [[False]*N for _ in range(M)]

    stack = []

    cnt = 0

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1 and not visited[i][j]:
                stack.append((i, j))

                while stack:
                    x, y = stack.pop()
                    
                    if not visited[x][y]:
                        visited[x][y] = True
                        
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            
                            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] == 1:
                                stack.append((nx, ny))
                cnt += 1

    # 결과 출력
    print(cnt)
