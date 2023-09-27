from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Logout')
    else:
        form = UserCreationForm()

    return render(request, 'BlogApplication/Signup.html')


# def loginView(request):
#     form = AuthenticationForm()
#     if request.method == "POST":
#         # Get Prepared Django Login Form and fill it with user's data coming from POST request
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
# # Validate username and password (user credentials)
#             user = authenticate(username=username, password=password)
# # If the user is authenticated
#             if user is not None:
#                 # This User will be logged in and will be
#                 login(request, user)
#         # Will be Redirected to Home page showing a success message
#                 return redirect("posts")

#     return render(request, "BlogApplication/LoginPage.html", context={"form": form})
