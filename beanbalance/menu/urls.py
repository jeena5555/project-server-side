from django.urls import path
from menu.views import MenuView, PaymentView, MenuManageView, editMenuView

urlpatterns = [
    path('', MenuView.as_view(), name="menu"),
    path('payment/', PaymentView.as_view(), name="payment"),
    path('manage/', MenuManageView.as_view(), name="manage"),
    path('manage/', editMenuView.as_view(), name='edit_menu'),
    # path('logout', LogoutView.as_view(), name="logout"),
    # path('test', TestView.as_view(), name="test")
]
