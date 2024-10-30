from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View

from accounts.models import Address, Information, Wallet
from custom_mixing.customize_mixing import UserLoginMixin


# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html', context={})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        error = 'username or password is not correct'
        return render(request, 'accounts/login.html', context={'error': error})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')


class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html', context={})

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = authenticate(username=username, password=password1)
        if user is not None:
            error_user = 'username is already taken'
            return render(request, 'accounts/register.html', context={'error_user': error_user})
        elif password1 != password2:
            error_password = 'passwords do not match'
            return render(request, 'accounts/register.html', context={'error_password': error_password})
        elif user is None:
            user = User.objects.create_user(username, email, password1)
            Information.objects.create(user=user)
            Wallet.objects.create(user=user)
            login(request, user)
            return redirect('home:home')


class AddressView(UserLoginMixin, View):
    def get(self, request):
        return render(request, 'accounts/give_address.html', context={})

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        postal_code = request.POST.get('postal_code')
        Address.objects.create(user = request.user, address=address, phone=phone, postal_code=postal_code)
        return redirect('home:home')
