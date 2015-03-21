from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post
from django.http import Http404

# Create your views here.

def lista(request):
    posts = Post.objects.all()
    contexto = {'posts': posts}
    return render_to_response("lista.html", contexto)
    
def detalle(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Este post no existe")
    contexto = {'post' : post}
    return render_to_response("detalle.html", contexto)