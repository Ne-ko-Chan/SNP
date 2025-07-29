import datetime

def date_in_future(integer) -> str:
    now = datetime.datetime.now()
    if not isinstance(integer, int):
        return now.strftime("%d-%m-%Y %H:%M:%S")

    td = datetime.timedelta(days=integer)
    return (now+td).strftime("%d-%m-%Y %H:%M:%S")

print(date_in_future([]))
print(date_in_future(2))
