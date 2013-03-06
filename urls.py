from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('quameteratlas.views',
    url(r'^index/$', 'index', name='index'),
    #url(r'^(?P<path>.*)$', 'directory', name='directory'),
    url(r'^directory/$', 'directory', name='directory'),
    #url(r'^list/$', 'list', name='list'),
)
