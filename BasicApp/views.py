from django.views.generic.base import View 
from django.http import HttpResponse
from .models import PersonInfoForm,PersonInfo
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.generic.edit import CreateView,FormView,UpdateView
from django.core.urlresolvers import reverse

class PersonInfoCreateView(CreateView):
    model=PersonInfo
    success_url='/thanks/'

    def form_valid(self,form):
        print "form is valid"
        return super(PersonInfoCreateView,self).form_valid(form)
    def form_invalid(self,form):
        print "form is invalid"
        return super(PersonInfoCreateView,self).form_invalid(form)

class PersonInfoUpdateView(UpdateView):
    model=PersonInfo
    success_url='/uthanks/'


class MyView(View):
    form_class=PersonInfoForm
    initial={'Fname':'Deepak'}
    template_name="forms.html"
    def get(self,request,*args,**kwargs):
        ci=RequestContext(request)
        form_class=self.form_class(initial=self.initial)
        return render_to_response(self.template_name,
                {'form':form_class},
                ci
                )

    def post(self,request,*args,**kwargs):
        ci=RequestContext(request)
        form_class=self.form_class(request.POST)
        if form_class.is_valid():
            kwargs=form_class.cleaned_data
            PersonInfo.objects.create(**kwargs)
            return HttpResponse("Data has been saved successfully")
        return render_to_response(self.template_name,
                {'form':form_class},
                ci
                )

    
class PersonInfoFormView(FormView):
    template_name='forms.html'
    form_class=PersonInfoForm
    success_url='/thanks/'

    def form_valid(self,form):
        return super(PersonInfoFormView,self).form_valid(form)
