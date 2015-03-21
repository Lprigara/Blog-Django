from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post, ComentarioForm, Comentario
from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def lista(request):
    posts = Post.objects.all()
    contexto = {'posts': posts}
    return render_to_response("lista.html", contexto)
    
class ListPost(ListView):
    model = Post
    
def detalle(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Este post no existe")
    contexto = {'post' : post}
    return render_to_response("detalle.html", contexto)
    
class DetailPost(DetailView):
    model = Post
    
class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('home')
    
class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('home')
    
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    
class AddComment(FormView):
    form_class = ComentarioForm
    success_url = '/'
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        autor = form.cleaned_data['autor']
        mensaje = form.cleaned_data['mensaje']
        
        c = Comentario()
        p = Post.objects.get(pk=pk)
        
        c.post = p
        c.autor = autor
        c.mensaje = mensaje
        c.save()
        
        return super(AddComment, self).form_valid(form)