def solution(a, b):
    answer = 0
    sum_list = []
    for n in range(min(a, b), max(a,b)+1):
        sum_list.append(n)
    answer = sum(sum_list)
    return answer