day_of_the_week = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
days_of_the_month = [0,31,29, 31, 30,31,30,31,31,30,31,30,31]
def solution(a, b):
    days = 0
    for month in range(1, a):
        days+=days_of_the_month[month]
    days+=b
    return day_of_the_week[days%7]