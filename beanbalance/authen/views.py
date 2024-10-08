from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('test')
        else:
            messages.error(request, "Username or password is not correct")
            return render(request, 'login.html', {"form": form})

        return render(request,'login.html', {"form":form})



class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')


class TestView(View):

    def get(self, request):
        return render(request, 'test.html')
