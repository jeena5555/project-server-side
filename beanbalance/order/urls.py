from django.urls import path
from order.views import OrderHistoryView

urlpatterns = [
    path('', OrderHistoryView.as_view(), name="order_history"),
]
