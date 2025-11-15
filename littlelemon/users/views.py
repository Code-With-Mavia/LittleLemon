from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after signup
            return redirect('/restaurant/')  # redirect after signup
        # no else needed; form.errors will handle messages in template
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/restaurant/')  # redirect after login
        else:
            # keep this for invalid credentials
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

@login_required(login_url='/users/login/')
def logout_view(request):
    logout(request)
    return redirect('/users/login/')
