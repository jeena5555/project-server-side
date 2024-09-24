from django.urls import path

from authen.views import LoginView, LogoutView, TestView

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('test', TestView.as_view(), name="test")
]
