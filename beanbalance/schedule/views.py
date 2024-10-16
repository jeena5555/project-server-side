from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from schedule.forms import FilterEmployeeForm, ScheduleForm, EditScheduleForm
from schedule.models import Schedule

from datetime import datetime, date
import calendar

class ScheduleView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = "/authen/"
    permission_required = ["schedule.view_schedule"]

    template_name = 'schedule.html'

    def get(self, request, year=None, month=None):
        form = FilterEmployeeForm(request.GET or {'select': 'ALL'})
        schedules = self.get_filtered_schedules(form)

        # Get the current year and month, or use provided values
        today = datetime.today()
        year, month = self.get_year_and_month(year, month, today)

        # Get the calendar and date range for the month
        month_calendar, start_date, end_date = self.get_month_calendar_and_range(year, month)

        # Filter schedules by the selected month
        schedules = schedules.filter(date__range=[start_date, end_date])

        # Organize schedules by day
        schedule_data = self.organize_schedules_by_day(schedules)

        context = {
            'form': form,
            'today': today,
            'year': year,
            'month': month,
            'month_name': calendar.month_name[month],
            'month_calendar': month_calendar,
            'schedule_data': schedule_data,
        }
        return render(request, self.template_name, context)

    def get_filtered_schedules(self, form):
        """Filter schedules based on employee selection."""
        if form.is_valid():
            selected_value = form.cleaned_data['select']
            if selected_value == 'ALL':
                return Schedule.objects.all()
            return Schedule.objects.filter(employee_id=selected_value)
        return Schedule.objects.all()

    def get_year_and_month(self, year, month, today):
        """Return the valid year and month, or fallback to current year/month."""
        year = year or today.year
        month = month or today.month

        if month < 1:
            month = 12
            year -= 1
        elif month > 12:
            month = 1
            year += 1
        return year, month

    def get_month_calendar_and_range(self, year, month):
        """Return the month calendar and the start/end date for the month."""
        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_calendar = cal.monthdayscalendar(year, month)

        start_date = datetime(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]
        end_date = datetime(year, month, last_day)

        return month_calendar, start_date, end_date

    def organize_schedules_by_day(self, schedules):
        """Organize schedules by the day of the month."""
        schedule_data = {}
        for schedule in schedules:
            day = schedule.date.day
            schedule_data.setdefault(day, []).append(schedule)
        return schedule_data


class AddScheduleView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = "/authen/"
    permission_required = ["schedule.add_schedule"]
    template_name = 'add_schedule.html'

    def get(self, request, day, month, year):
        schedule_date = self.get_schedule_date(day, month, year)
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

    def get_schedule_date(self, day, month, year):
        """Return a date object for the given day, month, and year."""
        return date(year=int(year), month=int(month), day=int(day))


class EditScheduleView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = "/authen/"
    permission_required = ["schedule.change_schedule", "schedule.delete_schedule"]

    template_name = 'edit_schedule.html'

    def get(self, request, day, month, year):
        schedule_date = self.get_schedule_date(day, month, year)
        formset = EditScheduleForm(queryset=Schedule.objects.filter(date=schedule_date), initial=[{'date': schedule_date}])
        return render(request, self.template_name, {'formset': formset, 'date': schedule_date})

    def post(self, request, day, month, year):
        schedule_date = self.get_schedule_date(day, month, year)
        formset = EditScheduleForm(request.POST, queryset=Schedule.objects.filter(date=schedule_date))

        if formset.is_valid():
            self.save_formset(formset, schedule_date)
            return redirect('schedule')

        return render(request, self.template_name, {'formset': formset, 'date': schedule_date})

    def save_formset(self, formset, schedule_date):
        """Save the formset with the updated schedules."""
        instances = formset.save(commit=False)
        for instance in instances:
            instance.date = schedule_date
            instance.save()
        for obj in formset.deleted_objects:
            obj.delete()

    def get_schedule_date(self, day, month, year):
        """Return a date object for the given day, month, and year."""
        return date(year=int(year), month=int(month), day=int(day))
