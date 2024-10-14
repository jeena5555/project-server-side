from django.urls import path
from menu.views import MenuView, PaymentView, MenuManageView, editMenuView,MenuDeleteView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', MenuView.as_view(), name="menu"),
    path('payment/', PaymentView.as_view(), name="payment"),
    path('manage/', MenuManageView.as_view(), name="manage"),
    path('manage/update/<int:menu_id>/', editMenuView.as_view(), name='update_menu'),
    path('manage/delete/<int:menu_id>/', MenuDeleteView.as_view(), name='delete_menu'),
    path('manage/category/update/<int:category_id>/', CategoryUpdateView.as_view(), name='update_category'),
    path('manage/category/delete/<int:category_id>/', CategoryDeleteView.as_view(), name='delete_category'),
    # path('login', LoginView.as_view(), name="login"),
    # path('logout', LogoutView.as_view(), name="logout"),
    # path('test', TestView.as_view(), name="test")
]
