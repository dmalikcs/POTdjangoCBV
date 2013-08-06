from .models import Publisher,Author,Book
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from django.forms import ModelForm
from django.views.generic.edit import CreateView

class AuthorForm(ModelForm):
    class Meta:
        model=Author


class ThanksRedirectView(RedirectView):
    def get_redirect_url(self):
        return "/cbv/thanks/"


class AuthorFormView(FormView):
    template_name="authorformview.html"
    form_class=AuthorForm
    success_url='/cbv/thanks'
    def form_valid(self,form):
        print "form is valid"
        print form.cleaned_data
        return super(AuthorFormView,self).form_valid(form)


class AuthorCreateView(CreateView):
    model=Author    
    def get_success_url(self):
        return '/cbv/thanks/'
    def get_context_data(**kwargs):
        context=super(AuthorCreateView,self).get_context_data(**kwargs)
        context['Data']="Welcome to another type of data"
        return context

