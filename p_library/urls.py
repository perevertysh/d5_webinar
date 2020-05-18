from django.contrib import admin
from django.urls import path
from .views import AuthorEdit, AuthorList, author_create_many

app_name = 'p_library'
urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('author/create_many/', author_create_many,
         name='author_create_many'),
]