from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Author
from .forms import AuthorForm


class AuthorListView(LoginRequiredMixin, ListView):
    login_url = 'login_page'

    model = Author
    template_name = "library/authors_list.html"
    context_object_name = "authors"

def author_delete(request, id):
    if not request.user.role == 1:
       return HttpResponse('<h1>403 Forbidden</h1>') 
    author = Author.get_by_id(id)
    if len(author.books.all()) == 0:
        author.delete()
        return redirect('authors_list_page')
    else:
        return redirect('authors_list_page')



def new_author_view(request):
    if request.method == 'GET':
        return render(request, 'library/new_author.html', {'form': AuthorForm})
    elif request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('authors_list_page')
        
