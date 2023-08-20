from datetime import datetime, timedelta

def day_and_time(mins):
    dt = datetime(2023, 8, 20)  # Произвольная дата для определения начального дня недели
    # dt = datetime.strptime('Sunday 00:00', '%A %H:%M')
    dt += timedelta(minutes=mins)
    dt = datetime.strftime(dt, '%A %H:%M')
    return dt


print(day_and_time(-3))