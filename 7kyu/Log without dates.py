def check_logs(log):
    if len(log) == 0:
        return 0
    if len(log) == 1:
        return 1
    count = 1
    h, m, s = map(int, log[0].split(':'))
    start = h * 3600 + m * 60 + s
    for i in log[1:]:
        h, m, s = map(int, i.split(':'))
        current_time = h * 3600 + m * 60 + s
        if current_time <= start:
            count += 1
        start = current_time
    return count


check_logs(["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"])
