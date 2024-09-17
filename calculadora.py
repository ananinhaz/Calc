from datetime import datetime, timedelta

def validar_temp(time_str):
    for fmt in ('%H:%M', '%H%M'):
        try:
            datetime.strptime(time_str, fmt)
            return
        except ValueError:
            continue
    raise ValueError("Invalid time format. Use HH:mm, H:mm, or HHmm.")

def calculate_hours(start, end, break_time='00:00'):
    validar_temp(start)
    validar_temp(end)
    validar_temp(break_time)

    start_time = datetime.strptime(start, '%H:%M')
    end_time = datetime.strptime(end, '%H:%M')
    break_time = datetime.strptime(break_time, '%H:%M')

    if end_time < start_time:
        end_time += timedelta(days=1)

    delta = end_time - start_time
    break_hours = break_time.hour + break_time.minute / 60
    return delta.seconds / 3600 - break_hours
