import datetime


def date_str_to_datetime(date: str) -> datetime.date:
    try:
        return datetime.datetime.strptime(date, '%Y-%m-%d')
    except:
        pass
    try:
        return datetime.datetime.strptime(date, '%d-%m-%Y')
    except:
        pass
    try:
        return datetime.datetime.strptime(date, '%d/%m/%Y')
    except:
        pass
    try:
        return datetime.datetime.strptime(date, '%Y%m%d')
    except:
        pass
    try:
        return datetime.datetime.strptime(date, '%d%m%Y')
    except:
        pass
    raise ValueError('couldnt solve date str format')

def format_datestr_to_url(date: str):
    if date != '':
        return date_str_to_datetime(date).strftime("%Y-%m-%d")
    else:
        return datetime.date.today().strftime("%Y-%m-%d")