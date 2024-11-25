def solution(mats, park):
    # 돗자리 크기 내림차순 정렬
    mats.sort(reverse=True)
    
    rows = len(park)
    cols = len(park[0])
    
    for size in mats:
        for i in range(rows):
            for j in range(cols):
                # (i, j) 위치에서 size 크기의 돗자리를 놓을 수 있는지 확인
                if i + size <= rows and j + size <= cols:
                    valid = True
                    for x in range(i, i + size):
                        for y in range(j, j + size):
                            if park[x][y] != "-1":  # 사람이 있는 자리
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        return size
    return -1
