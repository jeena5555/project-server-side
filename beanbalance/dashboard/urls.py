from django.urls import path
from dashboard.views import DashboardView, DashboardAllView

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('all', DashboardAllView.as_view(), name="dashboard_all"),
]
