from django.shortcuts import render, redirect
from django.views import View
from schedule.forms import FilterEmployeeForm, ScheduleForm
from schedule.models import Schedule

from datetime import datetime, date
import calendar

class ScheduleView(View):
    template_name = 'schedule.html'

    def get(self, request, year=None, month=None):
        form = FilterEmployeeForm(request.GET or {'select': 'ALL'})

        if form.is_valid():
            selected_value = form.cleaned_data['select']
            if selected_value == 'ALL':
                schedules = Schedule.objects.all()
            else:
                schedules = Schedule.objects.filter(employee_id=selected_value)
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

        # Fetching schedule data from the database for the current month
        schedules = schedules.filter(date__gte=start_date, date__lte=end_date)

        # Organize the data by day for easy display in the calendar
        schedule_data = {}
        for schedule in schedules:
            day = schedule.date.day

            if day not in schedule_data:
                schedule_data[day] = []
            schedule_data[day].append(schedule)

        # Get the month name (e.g., "January", "February")
        month_name = calendar.month_name[month]

        # Pass the calendar and other details to the template
        context = {
            'form': form,
            'today': today,
            'year': year,
            'month': month,
            'month_name': month_name,
            'month_calendar': month_calendar,
            'schedule_data': schedule_data,
        }

        return render(request, self.template_name, context)


class AddScheduleView(View):
    template_name = 'add_schedule.html'

    def get(self, request, day, month, year):
        schedule_date = date(year=int(year), month=int(month), day=int(day))

        # Create the form with an initial value for the date field
        form = ScheduleForm(initial={'date': schedule_date})

        context = {
            'form': form,
            'day': day,
            'month': month,
            'year': year,
        }

        return render(request, self.template_name, context)

    def post(self, request, day, month, year):
        form = ScheduleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('schedule')

        return self.get(request, day, month, year)


class EditScheduleView(View):
    template_name = 'edit_schedule.html'
    def get(self, request, day, month, year):
        schedule_date = date(year=int(year), month=int(month), day=int(day))

        form = ScheduleForm(initial={'date': schedule_date})

        schedule = Schedule.objects.get(date=schedule_date)

        context = {
            'form': form,
            'day': day,
            'month': month,
            'year': year,
        }

        return render(request, self.template_name, context)

    def put(self, request, day, month, year):
        form = ScheduleForm(request.POST)

        if form.is_valid():
            form.save()

        return self.get(request, day, month, year)

    def delete(self, request, day, month, year):
        form = ScheduleForm(request.POST)

        if form.is_valid():
            form.save()

        return self.get(request, day, month, year)
