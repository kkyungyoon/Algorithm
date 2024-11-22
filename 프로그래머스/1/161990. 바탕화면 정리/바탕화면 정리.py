def solution(wallpaper):
    # 초기화
    min_row, min_col = float('inf'), float('inf')
    max_row, max_col = float('-inf'), float('-inf')
    
    for row_idx, row in enumerate(wallpaper):
        for col_idx, cell in enumerate(row):
            if cell == '#':
                min_row = min(min_row, row_idx)
                min_col = min(min_col, col_idx)
                max_row = max(max_row, row_idx)
                max_col = max(max_col, col_idx)
    # 드래그 시작점, 끝점
    lux, luy = min_row, min_col
    rdx, rdy = max_row + 1, max_col + 1  
    
    return [lux, luy, rdx, rdy]
