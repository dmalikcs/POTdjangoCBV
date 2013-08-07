from .models import Publisher,Author,Book,Article
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from django.forms import ModelForm
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView

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


class AuthorUpdateView(UpdateView):
    model=Author
    success_url=reverse_lazy('author-list')
    template_name='author_update.html'


class AuthorDeleteView(DeleteView):
    model=Author
    success_url=reverse_lazy('author-list')

class AuthorListView(ListView):
    model=Author
    context_object_name='authors'

class AuthorDetailView(DetailView):
    model=Author
    context_object_name='author'


class ArticleArchiveIndexView(ArchiveIndexView):
    model=Article
    date_field="pub_date"
    allow_future=True
class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
