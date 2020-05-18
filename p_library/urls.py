from django.contrib import admin
from django.urls import path
from .views import AuthorCreate, AuthorRead, author_create_many, AuthorUpdate, AuthorDelete

app_name = 'p_library'

urlpatterns = [
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/', AuthorRead.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(),
         name='author_delete'),
    path('author/create_many/', author_create_many,
         name='author_create_many')
]
