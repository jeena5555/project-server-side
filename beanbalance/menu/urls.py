from django.urls import path
from menu.views import MenuView

urlpatterns = [
    path('', MenuView.as_view(), name="menu"),
    # path('payment', PaymentView.as_view(), name="payment"),
    # path('logout', LogoutView.as_view(), name="logout"),
    # path('test', TestView.as_view(), name="test")
]
