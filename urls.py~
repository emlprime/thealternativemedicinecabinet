from django.conf.urls.defaults import *
from django.contrib import admin

from thealternativemedicinecabinet.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template':'index.html'}),
    (r'^background/$', 'direct_to_template', {'template':'background.html'}),
    (r'^speaking/$', 'direct_to_template', {'template':'speaking.html'}),
    (r'^health_tips/$', 'direct_to_template', {'template':'health_tips.html'}),
    (r'^books/$', 'direct_to_template', {'template':'books.html'}),
    (r'^dvds/$', 'direct_to_template', {'template':'dvds.html'}),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += patterns('',
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/(.*)$', admin.site.root),
)
