from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _


def home(request):
    output = _("Hello, I'm Deepak Malik")
    return render_to_response(
        'index.html',
        {},
    )
