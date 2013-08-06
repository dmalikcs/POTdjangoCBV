from django.views.generic import ListView,DetailView
from Books.models import Publisher,Book,Author
from django.views.generic.base import View,TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse

class PublisherList(ListView):
    model=Publisher
    def get_context_data(self,**kwargs):
        context=super(PublisherList,self).get_context_data(**kwargs)
        context['Books']=Book.objects.all()
        context['Authors']=Author.objects.all()
        print context
        return context

class PulisherDetailView(DetailView):
    model=Publisher
    context_object_name = 'publisher'


class BooksView(View,TemplateResponseMixin):
    template_name="BookView.html"
    def get(self,request,*args,**kwargs):
        context={'dd':'Deepak Malik'}
        return self.render_to_response(context)
       
class OneBookView(View,SingleObjectMixin):
    model=Book
    context_object_name='book'
    def get(self,request,*args,**kwargs):
        return HttpResponse("Working")
