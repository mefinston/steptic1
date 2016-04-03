from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
   url(r'^$', views.error404),
   url(r'^login/$', views.error404),
   url(r'^signup/$', views.error404),
   url(r'^question/([0-9]{3})/$', views.test ),
   url(r'^ask/$', views.error404),
   url(r'^popular/$', views.error404),
   url(r'^new/$', views.error404),

)
