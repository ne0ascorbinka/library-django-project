from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .forms import LoginForm, SignUpForm

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
        

def logout_view(request):
    logout(request) 
    return redirect('homepage')   

def signin_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'library/signin.html', {'form': SignUpForm})
    elif request.method == 'POST':
        form = SignUpForm(request.POST) 
        if not form.is_valid():
           print(form.errors)
           print(repr(form.errors))
           return render(request, 'library/signin.html', {'form': form})
        
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
        
