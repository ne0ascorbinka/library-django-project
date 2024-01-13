from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Book
from .forms import BookForm
from author.models import Author

class BooksListView(ListView):
    model = Book
    template_name = 'library/books.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context


def add_book(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'library/new_book.html', {
            'form' : BookForm()
        })  
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('books_list')

def book_delete(request: HttpRequest, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('books_list')   

def detailed_book(request: HttpRequest, id):
    if not request.user.is_authenticated:
        return HttpResponse('<h1>403 Forbidden</h1>')    
    book = Book.get_by_id(id)
    context = {'book': book}
    return render(request, 'library/detailed_book.html', context)

def add_author_view(request: HttpRequest, id):
    if request.method == 'POST':
        author_id = int(request.POST['add_author'])
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=id)
        book.authors.add(author)
        return redirect('books_list')

def books_view(request: HttpRequest):
    """!DEPRECATED!"""
    if request.method == 'GET':
        books = list(Book.objects.all().order_by('id'))
        authors = list(Author.objects.all())
        context = {'books': books, 'authors': authors}
        return render(request,'library/books.html', context)
