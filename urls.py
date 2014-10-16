from django.conf.urls.defaults import *
from django.contrib import admin

from thealternativemedicinecabinet.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template':'index.html'}),
    (r'^background/$', 'direct_to_template', {'template':'background.html'}),
    (r'^disclaimer/$', 'direct_to_template', {'template':'disclaimer.html'}),
    (r'^television/$', 'direct_to_template', {'template':'television.html'}),
    (r'^free_gift/$', 'direct_to_template', {'template':'free_gift.html'}),
    (r'^books/$', 'redirect_to', {'url':'/store/'}),
    (r'^dvds/$', 'redirect_to', {'url':'/store/'}),
    (r'^store/$', 'direct_to_template', {'template': 'store.html'}),
    (r'^press/$', 'direct_to_template', {'template': 'press.html'}),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
urlpatterns += patterns('thealternativemedicinecabinet.content.views',
    (r'^consult/$', 'consult'),
    (r'^speaking/$', 'speaking'),
    (r'^health_tips/$', 'health_tips'),
    (r'^email/add/$','email_add'),
    (r'^media/$', 'media'),
    (r'^recommended_resources/$', 'recommended_resources'),
)

urlpatterns += patterns('',
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/(.*)$', admin.site.root),
)
