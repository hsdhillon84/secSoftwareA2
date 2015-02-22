from django.conf.urls import patterns, include, url
from secSoftwareA2.views import *
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'), 
    url(r'^logout/$', logout_page), 
    url(r'^register/$', register),
    #url(r'^register_user/$', register_user),
    url(r'^register/success/$', register_success),
    url(r'^update/$', update),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name= 'password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^home/$', home),
)