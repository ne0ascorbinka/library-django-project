"""
This module is becoming deprecated in context of
app views
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest
from book.models import Book
from authentication.models import CustomUser
from order.models import Order
from book.models import Book
from author.models import Author
from .forms import LoginForm, SignUpForm
from django.utils import timezone
from datetime import timedelta

def homepage_view(request):
    return render(request,'library/homepage.html')

def login_view(request:HttpRequest):
    if request.method == 'GET':
       return render(request, 'library/login.html', {'form': LoginForm})
    elif request.method == 'POST':
        
        form = LoginForm(request.POST)
        if form.is_valid():
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           user = authenticate(email=email, password=password)
           if user is not None:
              login(request, user)
              return redirect('homepage')
           else:
              return render(request, 'library/login.html', {'form': form, 'error_message': 'Wrong credentials, try again.'})
        else:
            return render(request, 'library/login.html', {'form': form, 'error_message': 'Wrong credentials, try again.'})
        
def books_view(request):
    if request.method == 'GET':
        books = list(Book.objects.all().order_by('id'))
        authors = list(Author.objects.all())
        context = {'books': books, 'authors': authors}
        return render(request,'library/books.html', context)  

def book_delete(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('books_list')   

def logout_view(request):
    logout(request) 
    return redirect('homepage')   

def add_book(request):
    if request.method == 'GET':
        return render(request, 'library/new_book.html')  
    elif request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        book = Book.create(name=name, description=description)
        return redirect('books_list')

def signin_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'library/signin.html', {'form': SignUpForm})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            middle_name = form.cleaned_data.get('middle_name', 'unknown')

            try:
                new_user = CustomUser.create(email=email, password=password,
                                                          first_name=first_name, last_name=last_name,
                                                          middle_name=middle_name)
                login(request, new_user)
                return redirect('homepage')
            except Exception as e:
                return HttpResponse(f'<h1>Error\n{e}</h1>')
        else:
           return render(request, 'library/signin.html', {'form': SignUpForm, 'error_message': 'Invalid credentials'})

        
def orders_view(request):
    if not request.user.is_authenticated:
        return HttpResponse('<h1>403 Forbidden</h1>')
    if request.user.role == 0:

        orders = list(Order.get_not_returned_books().filter(user_id = request.user.id))
    else:    
        orders = list(Order.get_not_returned_books())
    context = {'orders': orders}
    return render(request, 'library/orders.html', context)

def add_author_view(request, id):
    if request.method == 'POST':
        author_id = int(request.POST['add_author'])
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=id)
        book.authors.add(author)
        return redirect('books_list')
    
def new_author_view(request):
    if request.method == 'GET':
        return render(request, 'library/new_author.html')  
    elif request.method == 'POST':
        name = request.POST['name']  
        surname = request.POST['surname']
        patronymic =  request.POST['patronymic']
        Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        return redirect('authors_list_page')
    
def authors_list_view(request):
    if not request.user.is_authenticated:
        return HttpResponse('<h1>403 Forbidden</h1>')    
    authors =  list(Author.objects.all())
    context = {'authors': authors}
    return render(request, 'library/authors_list.html', context)

def author_delete(request, id):
    if not request.user.role == 1:
       return HttpResponse('<h1>403 Forbidden</h1>') 
    author = Author.get_by_id(id)
    if len(author.books.all()) == 0:
        author.delete()
        return redirect('authors_list_page')
    else:
        return redirect('authors_list_page')

def create_order_view(request, id):
    if not request.user.is_authenticated:
        return HttpResponse('<h1>403 Forbidden</h1>')
    if request.method == 'POST':
        current_time = timezone.now()
        plated_end_at = current_time + timedelta(days=14)
        book = Book.get_by_id(id)
        order = Order.create(user=request.user,book=book, plated_end_at=plated_end_at)
        if order:
            book.count -= 1
            book.save()
            return redirect('orders_page')

def detailed_book(request, id):
    if not request.user.is_authenticated:
        return HttpResponse('<h1>403 Forbidden</h1>')    
    book = Book.get_by_id(id)
    context = {'book': book}
    return render(request, 'library/detailed_book.html', context)

def close_order(request, id):
    if request.user.role != 1:
        return HttpResponse('<h1>403 Forbidden</h1>')
    order = Order.get_by_id(id)
    order.update(end_at=timezone.now())
    order.book.count += 1
    order.book.save() 
    return redirect('orders_page')        