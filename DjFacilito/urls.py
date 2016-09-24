from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjFacilito.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'TodoList.views.home', name='home'),
    url(r'^$', 'TodoList.views.log_in', name='log_in'),
    url(r'^login$', 'TodoList.views.log_in', name='login'),
    url(r'^logout/$', 'TodoList.views.log_out', name='log_out'),
    url(r'^registrar/$', 'TodoList.views.registrar', name='registrar'),
    url(r'^crear/$', 'TodoList.views.crear', name='crear'),
    url(r'^cumplir/(?P<pk>\d+)/$', 'TodoList.views.cumplir', name="cumplir"),
    url(r'^editar/(?P<pk>\d+)/$', 'TodoList.views.editar', name="editar"),
    url(r'^borrar/(?P<pk>\d+)/$', 'TodoList.views.borrar', name="borrar"),
    url(r'^nueva_categoria/$', 'TodoList.views.nueva_categoria', name='nueva_categoria'),



)
