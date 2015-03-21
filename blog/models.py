from django.db import models

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