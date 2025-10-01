from django.shortcuts import render

def home_page(request):
    return render(request, "athena/home.html")

# Create your views here.
