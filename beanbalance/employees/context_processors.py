from datetime import datetime

def current_date(request):
    now = datetime.now()
    return {
        'current_date': now,
        'current_month': now.strftime('%B'),
        'current_day': now.day,
        'current_weekday': now.strftime('%a'),
        'current_year': now.year
    }

