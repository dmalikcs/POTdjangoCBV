from django.conf.urls import patterns, include, url
from BasicApp.views import MyView
from BasicApp.views import PersonInfoCreateView,PersonInfoFormView,PersonInfoUpdateView
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'POTdjangoCBV.views.home', name='home'),
    # url(r'^POTdjangoCBV/', include('POTdjangoCBV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thanks/', TemplateView.as_view(
        template_name='thanks.html'
        ),name='thanks'),
    url(r'^uthanks/', TemplateView.as_view(
        template_name='uthanks.html'
        ),name='uthanks'),
    url(r'^$',MyView.as_view()),
    url(r'^create/',PersonInfoCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$',PersonInfoUpdateView.as_view()),
    url(r'^books/', include('Books.urls')),
    url(r'^cbv/', include('CBVTest.urls')),
    )
