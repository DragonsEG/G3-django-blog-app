from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user account
            # Add the user to the admin group
            adminGroup = Group.objects.get(name='Admin')  # Get the Admin group from the database
            user.groups.add(adminGroup)  # Add the user to the Admin group

            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'BlogApplication/Signup.html')
