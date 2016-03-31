from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lista/', 'cms.views.listado'),
    url(r'^nueva/', 'cms.views.nueva'),
    url(r'(\d+)','cms.views.pagina'),
    url(r'/?(.*)', 'cms.views.index'),
)
