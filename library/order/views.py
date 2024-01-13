from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from datetime import timedelta
from .models import Order
from .forms import OrderForm
from book.models import Book

def orders_view(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponse('<h1>403 Forbidden</h1>')
    if request.user.role == 0:

        orders = list(Order.get_not_returned_books().filter(user_id = request.user.id))
    else:    
        orders = list(Order.get_not_returned_books())
    context = {'orders': orders}
    return render(request, 'library/orders.html', context)

def create_order_view(request: HttpRequest, id):
    if not request.user.is_authenticated:
        return HttpResponse('<h1>403 Forbidden</h1>')
    

    if request.method == 'GET':
        book = Book.get_by_id(id)
        form = OrderForm(initial={'book' : book})
        return render(request, 'library/new_order.html', context={
            'form' : form,
            'id' : id
        })
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if not form.is_valid():
            return HttpResponse('<h1>Error: somehow form wasn\'t valid</h1>')
        book: Book = form.cleaned_data['book']
        current_time = timezone.now()
        plated_end_at = current_time + timedelta(days=14)
        order = Order.create(user=request.user, book=book, plated_end_at=plated_end_at)
        if order:
            book.count -= 1
            book.save()
            return redirect('orders_page')