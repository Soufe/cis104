from datetime import datetime
def get_weekday(date_str):
    date_object = datetime.strptime(date_str, '%d-%m-%Y')
    weekday_full = date_object.strftime('%A')
    weekday_camel_case = ''.join(word.capitalize() for word in weekday_full.split())
    return weekday_camel_case