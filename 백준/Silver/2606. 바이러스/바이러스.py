N = int(input())
M = int(input())

# 그래프 초기화
graph = {i: [] for i in range(1, N+1)} 

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 체크
visited = [False] * (N+1)
# 현재 위치 저장
stack = [1]
# 현재 노드 방문처리
visited[1] = True

while stack:
    current = stack.pop()
    for node in graph[current]:
        if not visited[node]:
            visited[node] = True
            stack.append(node)

print(sum(visited) - 1)