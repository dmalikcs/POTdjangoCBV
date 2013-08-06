from .models import Publisher,Author,Book
from django.views.generic.base import RedirectView


class ThanksRedirectView(RedirectView):
    def get_redirect_url(self):
        return "/cbv/thanks/"

