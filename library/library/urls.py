"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import homepage_view, login_view, logout_view, signin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='homepage'),
    path('author/', include('author.urls')),
    path('book/', include('book.urls')),
    path("order/", include('order.urls')),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout'),
    path('signin/', signin_view, name='signin_page'),
    # path('order/<int:id>', close_order, name='close_order' )
]
