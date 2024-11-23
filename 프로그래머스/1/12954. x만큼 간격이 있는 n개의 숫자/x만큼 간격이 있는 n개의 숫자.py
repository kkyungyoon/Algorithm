def solution(x, n):
    answer = []
    answer.append(x)
    st_x = x
    for i in range(1,n):
        x = st_x + st_x*i
        answer.append(x)
    return answer