from datetime import timedelta

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)

def vacationPeriod(begin,end):
    if begin.month == end.month and begin.year == end.year:
        return True
    else:
        result = []
        while True:
            if begin.month == 12:
                next_month = begin.replace(year=begin.year+1,month=1, day=1)
            else:
                next_month = begin.replace(month=begin.month+1, day=1)
            if next_month > end:
                break
            result.append ([begin.strftime("%Y-%m-%d"),last_day_of_month(begin).strftime("%Y-%m-%d")])
            begin = next_month
        result.append ([begin.strftime("%Y-%m-%d"),end.strftime("%Y-%m-%d")])
        return result
