from django.contrib import admin
from .models import Post, Comentario

# Register your models here.

#fd
class ComentarioInline(admin.StackedInline):
    model = Comentario
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    inlines = [ComentarioInline]
    date_hierachy = 'fecha'

admin.site.register(Post, PostAdmin)
