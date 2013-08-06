from django.db import models
from django.forms import ModelForm

# Create your models here.

class PersonInfo(models.Model):
    Fname=models.CharField(max_length=30,
            verbose_name="First Name",
            )
    Lname=models.CharField(max_length=40,
            verbose_name="Last Name",
            )
    email=models.EmailField(max_length=75,
            verbose_name="Email",
            )
    Message=models.TextField(max_length=75,
            verbose_name="Messaage"
            )
    def __unicode__(self):
        return self.Fname

class PersonInfoForm(ModelForm):
    class Meta:
        model=PersonInfo
