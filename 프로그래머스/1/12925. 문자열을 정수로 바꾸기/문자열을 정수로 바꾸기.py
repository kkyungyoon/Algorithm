def solution(s):
    answer = 0
    if '-' in s:
        answer = -int(s[1:])
    else:
        answer = int(s)
    return answer