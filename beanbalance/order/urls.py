from django.urls import path
from order.views import OrderHistoryView

urlpatterns = [
    path('', OrderHistoryView.as_view(), name="order_history"),
    # path('logout', LogoutView.as_view(), name="logout"),
    # path('test', TestView.as_view(), name="test")
]
