from django.conf.urls.defaults import *

urlpatterns = patterns('openlabs.views',
    url(r'^$', 'portfolio', name='portfolio'),
)
