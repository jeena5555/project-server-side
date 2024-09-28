from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from menu.models import Menu, Category

# Create your views here.

class MenuView(View):
    template_name = "menu.html"

    def get(self, request):
        menus = Menu.objects.all()[:10]
        categories = Category.objects.all()
        context = {
            "menus": menus,
            "categories": categories
        }
        return render(request, self.template_name, context)

@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Here you would typically update the cart in the session or database
        # For this example, we'll just return the received data
        return JsonResponse({'status': 'success', 'cart': data})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# class PaymentView(View):
#     template_name = "payment.html"

#     def get(self, request):
#         menus = Menu.objects.all()[:5]
#         for i in menus:
#             print(i)
#         context = {
#             "orders": menus
#         }
#         return render(request, self.template_name, context)
