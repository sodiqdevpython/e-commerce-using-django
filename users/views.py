from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import LoginForm, SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            get_data = form.cleaned_data
            form.save()
            new_user = authenticate(request, username=get_data['username'], password=get_data['password1'])
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, "Parol foydalanuvchi nomiga juda o'xshash bo'lmasin.")
            messages.error(request, "Parol kamida 8 ta belgidan iborat boʻlishi kerak.")
            messages.error(request, "Parol juda oddiy bo'lmasligi kerak.")
            return redirect('signup')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            get_data = form.cleaned_data
            get_user_number = (get_data['username']).split(' ')
            user_number = ''
            for char_user_number in get_user_number:
                user_number += char_user_number
            user = authenticate(request, username=user_number, password=get_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Telefon raqamingiz yoki parol xato')
                return redirect('login')
        else:
            return HttpResponse(form.errors)
    else:
        form = LoginForm()

    return render(request, 'signin.html', {'form': form})

"""
The two password fields didn’t match
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
"""