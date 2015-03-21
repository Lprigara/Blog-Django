from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import ListPost, DetailPost, PostCreate, PostDelete, PostUpdate, AddComment
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'blog.views.lista', name='home'),
#    url(r'^detalle/(?P<pk>\d+)$', 'blog.views.detalle', name='detalle'),  #?p : se le pasa un parametro
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ListPost.as_view(template_name='listpost.html'), name='home'),
    url(r'^detalle/(?P<pk>\d+)$', DetailPost.as_view(template_name='detailpost.html'), name='detalle'),  #?p : se le pasa un parametro
    url(r'post/create$', login_required(PostCreate.as_view(template_name='post_form.html')), name='create_post'),
    url(r'post/(?P<pk>\d+)/update$', login_required(PostUpdate.as_view(template_name='post_form.html')), name='update_post'),
    url(r'post/(?P<pk>\d+)/delete$', login_required(PostDelete.as_view(template_name='post_form.html')), name='delete_post'),
    url(r'post/(?P<pk>\d+)/add_comment$', AddComment.as_view(template_name='add_comentario.html'), name='add_comment'),
    
    
    url(r'^admin/', include(admin.site.urls)),
)
