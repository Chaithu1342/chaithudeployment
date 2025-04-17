from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Home redirect

def home_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('chaithu_app:dashboard')
    return redirect('chaithu_app:login')

# General views

def home(request):
    return render(request, 'chaithu_app/home.html')

def about_view(request):
    return render(request, 'chaithu_app/about.html')

def account_view(request):
    return render(request, 'chaithu_app/account.html')

def account_settings_view(request):
    return render(request, 'chaithu_app/account_settings.html')

def change_password_view(request):
    return render(request, 'chaithu_app/change_password.html')

def contact_view(request):
    return render(request, 'chaithu_app/contact.html')

def dashboard_view(request):
    return render(request, 'chaithu_app/dashboard.html')

def index(request):
    return render(request, 'chaithu_app/index.html')

def settings_view(request):
    return render(request, 'chaithu_app/settings.html')

def preferences_view(request):
    return render(request, 'chaithu_app/preferences.html')

def profile_view(request):
    return render(request, 'chaithu_app/profile.html')

def registration(request):
    return render(request, 'chaithu_app/registration.html')

# Auth views

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chaithu_app:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'chaithu_app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'chaithu_app:dashboard')
            return redirect(next_url)
        else:
            return render(request, 'chaithu_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chaithu_app/login.html')
    return redirect('chaithu_app:profile')  # Redirect to profile or another page


def logout_view(request):
    logout(request)
    return redirect('chaithu_app:login')
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChangePasswordForm

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            # Process the password change
            # For example, update the user's password in the database
            new_password = form.cleaned_data['new_password']
            # Here you should update the password of the logged-in user, e.g.:
            request.user.set_password(new_password)
            request.user.save()

            # Optionally log the user out after changing the password
            messages.success(request, "Your password has been successfully changed.")
            return redirect('chaithu_app:login')  # Or any other appropriate page

        else:
            messages.error(request, "There was an error with your form.")
    else:
        form = ChangePasswordForm()

    return render(request, 'chaithu_app/change_password.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User is authenticated
                login(request, user)
                messages.success(request, "You are now logged in!")
                return redirect('chaithu_app:profile')  # Or another page to redirect after login
            else:
                # Authentication failed
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill in both fields.")
    else:
        form = LoginForm()

    return render(request, 'chaithu_app/login.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Try to authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                messages.success(request, "You are now logged in!")
                return redirect('chaithu_app:profile')  # Redirect after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill in both fields.")
    else:
        form = LoginForm()

    return render(request, 'chaithu_app/login.html', {'form': form})
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('chaithu_app:profile')  # Redirect to profile if already logged in

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in!")
                return redirect('chaithu_app:profile')  # Redirect after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill in both fields.")
    else:
        form = LoginForm()

    return render(request, 'chaithu_app/login.html', {'form': form})
# chaithu_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('chaithu_app:profile')  # Redirect to profile page if the user is already logged in

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, "You are now logged in!")
                return redirect('chaithu_app:profile')  # Redirect to the profile page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please fill in both fields.")
    else:
        form = LoginForm()

    return render(request, 'chaithu_app/login.html', {'form': form})
