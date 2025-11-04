from django.shortcuts import render
from django.shortcuts import redirect

from .models import Post
from .forms import PostCreateform

# Create your views here.
def editor_texto(request):
    if request.method == "POST":
        form = CriarPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        
        else:
            form = CriarPost()
        #Quando estiver com o frontend pronto coloca dentro do parâmetro do render!
        return render()