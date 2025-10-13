from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

def home_page(request):
    return render(request, "athena/home.html")

def loginPage(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name,password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            context['error'] = "Nome de usuario incorreto"

    return render(request, "athena/login.html", context)

def registerPage(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not name or not email or not password:
            context['error'] = "preencha todos os campos"
            return render(request, "athena/register.html",context)
        elif User.objects.filter(username=name).exists():
            context['error'] = "um usuario com esse nome ja existe"
            return render(request, "athena/register.html",context)
        
        User.objects.create(username = name,email = email, password = password)
        return redirect('login')
    
    return render(request, "athena/register.html",context)

# Create your views here.
