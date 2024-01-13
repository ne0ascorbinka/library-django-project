from django import forms
from book.models import Book

class OrderForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label="Choose a book")
