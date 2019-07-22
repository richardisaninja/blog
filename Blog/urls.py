# from django.contrib import admin
from django.urls import path, include

from Blog import views

urlpatterns = [
    path('', views.view_posts, name='post_view'),
    path('create/', views.create, name='post_create'),
    path('update/<int:id>/', views.edit, name='post_update'),
    path('delete/<int:id>/', views.delete, name='post_delete'),
    path('comment/<int:id>/', views.create_comment, name='post_comment'),
]
