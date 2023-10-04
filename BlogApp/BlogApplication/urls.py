from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('', views.index, name='posts'),
    path('addaPost/', views.addPost, name='addPost'),
    path('editPost/<int:pk>', views.editPost, name='edit'),
    path('delete/<int:pk>', views.deletePost, name='delete'),
    path('postDetails/<int:pk>', views.postDetails, name='details'),
    path('publishPost/<int:pk>', views.publishPost, name='publishPost'),
    path('ShowCategories', views.showCategories, name='categories'),
    path('addaComment/<int:pk>', views.addComment, name='addComment'),
    path('addaCategory/', views.addCategory, name='addCategory'),
    path('editaCategory/<int:pk>', views.editCategory, name='editCategory'),
    path('deleteaCategory/<int:pk>', views.deleteCategory, name='deleteCategory'),
    path('viewCategories/', views.viewCategories, name='viewCategories'),
]
