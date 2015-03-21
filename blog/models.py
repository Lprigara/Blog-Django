from django.db import models
from django import forms
# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(null=True)
    
    def __unicode__(self):
        return "Post: {}, autor: {}".format(self.titulo, self.autor)
    
    
class Comentario(models.Model):
    post = models.ForeignKey(Post) #un comentario solo pertenece a un post
    autor = models.CharField(max_length=255)
    mensaje = models.TextField()
    
    def __unicode__(self):
        return "{} - {}".format(self.post.pk, self.mensaje[:15])
        
# Creando formulario propio
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'mensaje']
        widgets = {
            'mensaje':forms.Textarea(attrs={'cols':80, 'rows':20}), 
            }