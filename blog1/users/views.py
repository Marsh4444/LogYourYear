from django.shortcuts import render, redirect
from bloggss.models import Category, Blog
from .utils import user_in_group 
from .forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login , logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .decorators import group_required
from django.contrib.auth import get_user_model



# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context)


# def login_view(request):

#     #handle post request
#     form = AuthenticationForm(request, data=request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)

#             messages.success(request, "Login successful 🎉")

#             return redirect("home")
#         else:
#             messages.error(request, "Invalid username or password")
   
#2  
    # # #handle post request
    # if request.method == 'POST':
    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = auth.authenticate(username=username, password=password)
    #         if user is not None:
    #             auth.login(request, user)
    #             return redirect('home')

    # # #handle get request
    # form = AuthenticationForm()
    # context = {
    #     'form': form
    # }
    # return render(request, 'users/login.html', context)

def login_view(request):
    # Handle POST request
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, "Login successful 🎉")

            # 🔥 ROLE-BASED REDIRECT
            if user.groups.filter(name="Manager").exists():
                return redirect("manager_dashboard")

            elif user.groups.filter(name="Editor").exists():
                return redirect("editor_dashboard")

            elif user.groups.filter(name="Author").exists():
                return redirect("author_dashboard")

            else:
                messages.error(request, "No role assigned.")
                return redirect("home")  # fallback if no group

        else:
            messages.error(request, "Invalid username or password")

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def logout_view(request):
    # Log the user out
    auth_logout(request)

    # Add a success message
    messages.success(request, "You have successfully logged out.")

    # Redirect to home (or login page if you prefer)
    return redirect("home")

User = get_user_model()  # get the custom user model if you have one

@login_required
@group_required("Manager")# 1️⃣ Check if the user is in the Manager group redirect to home if not a manager
def manager_dashboard(request):

    # 2️⃣ Count total posts, categories, and users
    posts_count = Blog.objects.count()
    categories_count = Category.objects.count()
    users_count = User.objects.count()

    # 3️⃣ Prepare the context dictionary to pass to the template
    context = {
        "posts_count": posts_count,
        "categories_count": categories_count,
        "users_count": users_count,
    }

    # 4️⃣ Render the template with the context
    return render(request, "users/manager/dashboard.html", context)

@login_required
@group_required("Editor")
def editor_dashboard(request):
    return render(request, "users/editor/dashboard.html")


@login_required
@group_required("Author")
def author_dashboard(request):
    return render(request, "users/author/dashboard.html")