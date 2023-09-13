from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from account.forms import AccountRegistrationForm
from django.utils.decorators import method_decorator
from account.decorators import not_guest_only


@not_guest_only
def register_view(request):
    if request.method == 'POST':
        register_form = AccountRegistrationForm(request.POST)
        if not register_form.is_valid():
            print(register_form.errors)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = AccountRegistrationForm()
    return render(request, 'register.html', {'register_form': register_form})


@not_guest_only
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            login_form = AuthenticationForm()
            messages.error(request, f'Invalid username or password')
    else:
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect("login")
