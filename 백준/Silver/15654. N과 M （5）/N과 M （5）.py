N, M = map(int, input().split())
numbers = sorted(map(int, input().split())) # 1789

visited = [False]*N
result = []
stack = [([], visited[:])] # 초기화 (지금까지 방문한 노드, 방문상태)  

while stack:
    sequence, visited = stack.pop()
    # 가지치기 - 종료조건
    if len(sequence) == M:
        result.append(sequence)
        continue
        
    # 가지치기 - 역순으로 추가하여 사전 순 탐색
    for i in range(N-1, -1, -1): # N-1 : numbers[i] 인덱스 맞추려고
        if not visited[i]:
           new = sequence + [numbers[i]]
           new_visited = visited[:]
           new_visited[i] = True
           stack.append((new, new_visited))

for res in result:
    print(' '.join(map(str, res))) 