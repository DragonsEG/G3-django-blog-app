from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup/', views.signUp, name='userSignUp'),
    # path('login/', auth_view.LoginView.as_view(template_name='BlogApplication/Login.html'), name='userLogin'),
    path('logout/', auth_view.LogoutView.as_view(template_name='BlogApplication/Logout.html'), name='userLogout'),


]
