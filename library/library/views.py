"""
Module with some basic views
"""

from django.shortcuts import render
from django.http import HttpRequest

def homepage_view(request: HttpRequest):
    return render(request,'library/homepage.html')
