def solution(park, routes):
    answer = []
    H = len(park)       # 공원세로
    W = len(park[0])    # 공원가로

    # 초기 위치
    for i in range(H):
        if 'S' in park[i]:
            x, y = i, park[i].index('S')
            break

    # 방향 벡터
    direction = {'E': (0, 1),
                 'W': (0, -1),
                 'S': (1, 0),
                 'N': (-1, 0)}

    for route in routes:
        d, distance = route.split()
        dx, dy = direction[d]
        distance = int(distance)

        nx, ny = x, y
        valid_move = True

        for _ in range(distance):
            nx += dx
            ny += dy

            if nx < 0 or ny < 0 or nx >= H or ny >= W or park[nx][ny] == "X":
                valid_move = False
                break

        if valid_move:
            x, y = nx, ny
    answer.append(x)
    answer.append(y)
    return answer