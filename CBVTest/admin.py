from django.contrib import admin 
from .models import Publisher,Book,Author,Article

admin.site.register(Publisher)

admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Author)
