"""
DFS(깊이 우선 탐색) : 한 방향으로 깊게 탐색하고 더 탐색할 곳이 없으면 직전에 방문했던 노드로 되돌아가는 방식 
    - LIFO 
    - 스택사용(append, pop)
BFS(너비 우선 탐색) : 현재 노드와 인접한 노드들을 모두 탐색한 후, 다음 깊이로 넘어가는 방식 
    - FIFO 
    - 큐(append, popleft)
    - 최단거리 찾는데 효과적(이동시간 일정한 경우)
다익스트라 알고리즘 : 이동시간이 일정하지 않고, 각 이동 방식에 따라 시간이 다르게 주어지는 경우
"""
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().strip().split())

max_position = 100000

visited = [False]*(max_position+1) # 방문여부체크배열
queue = deque([(N, 0)]) # (현재 위치, 현재까지의 시간) # BFS 초기화
visited[N] = True

# BFS 탐색
while queue:
    position, time = queue.popleft()
    
    # 동생 찾을 때
    if position == K:
        print(time)
        break
    
    # 현재 position에서 이동가능한 모든 위치 계산
    for next_pos in (position-1, position+1, position*2):
        if 0 <= next_pos <= max_position and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, time+1))