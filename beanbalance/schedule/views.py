from django.shortcuts import render
from django.views import View

import calendar
from collections import defaultdict
from datetime import datetime

# Create your views here.

class ScheduleView(View):
    template_name = 'schedule.html'
    def get(self, request, year=None, month=None, day=None):
        # Get the current date or the date based on provided year and month
        today = datetime.today()
        year = year or today.year
        month = month or today.month

        if month < 1:
            month = 12
            year -= 1
        elif month > 12:
            month = 1
            year += 1

        # Generate calendar for the given month and year
        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_calendar = cal.monthdayscalendar(year, month)

        # Get the start and end date of the month
        start_date = datetime(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]  # Get the number of days in the month
        end_date = datetime(year, month, last_day)


        # Get the month name (e.g., "January", "February")
        month_name = calendar.month_name[month]

        # Pass the calendar and other details to the template
        context = {
            'today': today,
            'year': year,
            'month': month,
            'month_name': month_name,
            'month_calendar': month_calendar,
        }

        return render(request, self.template_name, context)
