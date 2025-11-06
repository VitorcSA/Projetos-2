from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Preferencias
# Create your views here.

@login_required 
def selecionar_interesses(request):
    todos_topicos= Preferencias.objcets.all()

    if request.method == 'POST' :

        interesses_id_selecionados = request.POST.getlist('Precerencias')

        user = request.user

        user.Preferencias.set(interesses_id_selecionados)

        return redirect('')
    
    context={
        'Todos os Interesses': todos_topicos
    }
    return render(request, '', context)