from django.db import models
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=15)
    bio = models.TextField(null=True, blank=True)
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    def published_recently(self):
        return now()- self.published_date <= timedelta(days=7)
    title = models.CharField(max_length=15)
    content = models.TextField(blank=True , null=False)
    published_date = models.DateTimeField()
    photo = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
    author = models.ForeignKey(Author , on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.title} , {self.published_date}"
    




    