from django.conf.urls import patterns, include, url
from .views import PublisherList,PulisherDetailView,BooksView,OneBookView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^publishers$', PublisherList.as_view(), name='publisher'),
    url(r'^books/$', BooksView.as_view(), name='BooksView'),
    url(r'^one/$', OneBookView.as_view(), name='OneBookView-url'),
    url(r'^publishers/(?P<pk>\d+)/$', PulisherDetailView.as_view(), name='publisher-detailview'),
    # url(r'^POTdjangoCBV/', include('POTdjangoCBV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    )
