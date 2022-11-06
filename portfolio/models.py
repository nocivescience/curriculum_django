from django.db import models

# Create your models here.

from django.db import models
from django.db.models.fields import CharField,URLField, DateField
from django.db.models.fields.files import ImageField
from datetime import date
class Project(models.Model):
    title= CharField(max_length=100)
    description=CharField(max_length=500)
    image=ImageField(
        upload_to='portfolio/images'
    )
    url=URLField(blank=True)
    date=DateField(default=date.today)
    def __srt__(self)->str:
        return self.title #modifica esto waxito
