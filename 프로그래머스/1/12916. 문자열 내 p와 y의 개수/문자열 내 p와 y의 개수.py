def solution(s):
    s = s.upper()
    cnt_p = s.count('P')
    cnt_y = s.count('Y')
    if cnt_p == cnt_y:
        return True
    elif cnt_p != cnt_y:
        return False
    else:
        return True