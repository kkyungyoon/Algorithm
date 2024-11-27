def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time_str):
        mm, ss = map(int, time_str.split(':'))
        return mm * 60 + ss

    video_len_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    op_start_sec = to_seconds(op_start)
    op_end_sec = to_seconds(op_end)

    for command in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            # 오프닝 구간이면 끝나는 시점으로 이동
            pos_sec = op_end_sec
        if command == "prev":
            # 10초 전으로 이동
            pos_sec = max(0, pos_sec - 10)
        elif command == "next":
            # 10초 후로 이동
            pos_sec = min(video_len_sec, pos_sec + 10)

        # 오프닝 구간에 재진입한 경우 처리
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    mm = pos_sec // 60
    ss = pos_sec % 60
    answer = f"{mm:02}:{ss:02}"

    return answer

