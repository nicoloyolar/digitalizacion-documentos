from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'usuarios/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            pass

    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)  
    return redirect('login') 

def home_view(request):
    
    return render(request, 'usuarios/home.html')

def documento2(request):
    return render(request, 'usuarios/documento2.html')