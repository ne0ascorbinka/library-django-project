from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthorListView.as_view(), name='authors_list_page'),
    path('delete/<int:id>', views.author_delete, name='delete_author'),
    path('add/', views.new_author_view, name='new_author_page'),

]
