from django.db import models

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(null=True)
    
    def __unicode__(self):
        return "Post: {}, autor: {}".format(self.titulo, self.autor)
    
    
