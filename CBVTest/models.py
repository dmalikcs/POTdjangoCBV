from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots',blank=True)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()


class Article(models.Model):
    title=models.CharField(max_length=30)
    pub_date=models.DateField()
    def __unicode__(self):
        return self.title
    #def get_absolute_url(self):
    #   return reverse('article-detail', kwargs={'pk': self.pk})
