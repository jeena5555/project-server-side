from django.urls import path
from order.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    # path('logout', LogoutView.as_view(), name="logout"),
    # path('test', TestView.as_view(), name="test")
]
