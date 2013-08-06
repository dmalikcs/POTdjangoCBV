from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from CBVTest.views import ThanksRedirectView
from CBVTest.views import AuthorFormView,AuthorCreateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^templateview/$', TemplateView.as_view(
        template_name="CBVTest.html"
        ),
        ),
    # url(r'^POTdjangoCBV/', include('POTdjangoCBV.foo.urls')),
    url(r'redirect/$',ThanksRedirectView.as_view()),
    url(r'thanks/$',TemplateView.as_view(
        template_name='thanks.html'
        ),
        name='cbvthanks'),
    url(r'authorform/$',AuthorFormView.as_view()),
    url(r'authorcreate/$',AuthorCreateView.as_view()),
   


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    )
