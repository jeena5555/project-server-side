from django.urls import path
from schedule.views import ScheduleView, AddScheduleView, EditScheduleView

urlpatterns = [
    path('', ScheduleView.as_view(), name="schedule"),
    path('schedule/<int:year>/<int:month>/', ScheduleView.as_view(), name='schedule'),
    path('add/<int:day>/<str:month>/<int:year>/', AddScheduleView.as_view(), name='add_schedule'),
    path('edit/<int:day>/<str:month>/<int:year>/', EditScheduleView.as_view(), name='edit_schedule'),
]
