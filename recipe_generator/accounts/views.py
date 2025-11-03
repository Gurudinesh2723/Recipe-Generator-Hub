from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe  # Import the Recipe model
from django.contrib import messages  # Import for success/error messages

# 🚨 REGISTER VIEW
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login the user after registration
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# 🚨 LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# 🚨 LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')

# 🚨 DASHBOARD VIEW (Improved Version with Recipe Display)
@login_required
def dashboard(request):
    # Fetch 5 most recent recipes for the logged-in user
    recent_recipes = Recipe.objects.filter(user=request.user).order_by('-created_at')[:5]

    # Handle empty state: If no recipes exist
    if not recent_recipes.exists():
        messages.info(request, "You haven't created any recipes yet.")

    return render(request, 'accounts/dashboard.html', {'recent_recipes': recent_recipes})

# 🚨 WELCOME PAGE VIEW
def welcome_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # ✅ If already logged in, go to dashboard
    return render(request, 'accounts/welcome.html')  # Otherwise show welcome page

