def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    
    term_dict = dict()
    for term in terms:
        term = term.split(' ')
        term_dict[term[0]] = term[1]
    
    for idx, privacy in enumerate(privacies):
        privacy = privacy.split(' ')
        alphabet = privacy[1]
        privacy = privacy[0].split('.')
        day = 28 * int(term_dict[alphabet])
        
        sub_year = 28 * 12 * (int(today[0]) - int(privacy[0]))
        sub_month = 28 * (int(today[1]) -int(privacy[1]))
        sub_day = int(today[2]) - int(privacy[2])
        total = sub_year + sub_month + sub_day
        
        if total >= day:
            answer.append(idx+1)
    return answer