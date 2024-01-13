from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('add/', views.add_book, name='new_book'),
    path('delete/<int:id>', views.book_delete, name='delete_book'),
    path('<int:id>', views.detailed_book, name='detailed_book'),
    path('assign_author/<int:id>', views.add_author_view, name='add_author'),
]
