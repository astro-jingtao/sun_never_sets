import functools
import datetime
import pytz
from tzwhere import tzwhere
from astral import LocationInfo, sun

def is_sun_on_sky(latitude, longitude, timezone, utc_time):
    observer = LocationInfo(latitude=latitude, longitude=longitude)
    utc_datetime = datetime.datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S')
    utc_datetime = utc_datetime.replace(tzinfo=pytz.utc)

    # to local time
    local_time = utc_datetime.astimezone(pytz.timezone(timezone))
    # print(f"Local time: {local_time}")

    # sunrise and sunset in local time
    # print(observer.observer)
    s = sun.sun(observer.observer, date=utc_datetime)

    if s['sunrise'] < s['sunset']:
        return s['sunrise'] < utc_datetime < s['sunset']
    else:
        return (utc_datetime > s['sunrise']) or (utc_datetime < s['sunset'])

def format_datetime(year, month, day, hour, minute, second):
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

def getBetweenDay(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    while begin_date <= end_date:
        # date_str = begin_date.strftime('%Y-%m-%d %H:%M:%S')
        date_list.append(begin_date)
        begin_date += datetime.timedelta(days=1)
    return date_list