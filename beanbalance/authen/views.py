from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import Group


class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            position = user.groups.first().name

            if position == "Manager":
                return redirect("dashboard")
            elif position == "Cashier":
                return redirect("menu")

        else:
            messages.error(request, "Username or password is not correct")
            return render(request, "login.html", {"form": form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login")
