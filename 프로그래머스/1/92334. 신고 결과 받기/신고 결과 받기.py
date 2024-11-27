def solution(id_list, report, k):
    # 동일한 유저에 대한 신고 횟수 1회로 처리
    report = list(set(report))
    
    # 유저가 신고당한 횟수를 저장
    reported_count = {user: 0 for user in id_list}
    
    # 유저가 신고한 유저 목록을 저장
    user_reports = {user: [] for user in id_list}
    
    for r in report:
        reporter, reported = r.split()
        if reported not in user_reports[reporter]:
            user_reports[reporter].append(reported)
            reported_count[reported] += 1
    
    # 정지된 유저 리스트
    suspended_users = [user for user, count in reported_count.items() if count >= k]
    
    # 유저가 신고한 유저 중 정지된 유저 수 계산
    result_mail_count = []
    for user in id_list:
        result_mail_count.append(len([u for u in user_reports[user] if u in suspended_users]))
    
    return result_mail_count