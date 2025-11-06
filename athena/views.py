from django.shortcuts import render, get_object_or_404
from .models import Noticia, Tag


def home_page(request):
    return render(request, "athena/home.html")

def noticias_por_tag(request, tag_slug):
   
    tag = get_object_or_404(Tag, slug=tag_slug)
    
   
    noticias = Noticia.objects.filter(tags=tag).order_by('-data_publicacao')
    
   
    context = {
        'tag': tag,
        'noticias': noticias
    }
    
    return render(request, 'athena/noticias_por_tag.html', context)

# Create your views here.
