from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post
# Create your views here.

def lista(request):
    posts = Post.objects.all()
    contexto = {'posts': posts}
    return render_to_response("lista.html", contexto)
    
def detalle(request, pk):
    post = Post.objects.get(pk=pk)
    contexto = {'post' : post}
    return render_to_response("detalle.html", contexto)