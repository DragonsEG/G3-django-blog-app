from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('', views.index, name='posts'),
    path('publishPost/<int:pk>', views.publishPost, name='publishPost'),
    path('addPost', views.renderAdd, name='add'),
    path('editPost/<int:pk>', views.editPost, name='edit'),
    path('delete/<int:pk>', views.deletePost, name='delete'),
    path('postDetails/<int:pk>', views.postDetails, name='details'),
    path('addaPost/', views.addPost, name='addPost'),
    path('addaComment/<int:pk>', views.addComment, name='addComment'),
]
