def solution(s):
    from collections import defaultdict
    answer = []
    D = defaultdict(lambda: -1) 

    for idx, al in enumerate(s):
        if D[al] == -1:
            answer.append(-1)
        else:
            answer.append(idx - D[al])
        D[al] = idx

    return answer
