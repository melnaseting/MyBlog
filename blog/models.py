from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextChoices()
    published_date = models.DateTimeField()
    photo = models.ImageField(upload_to='C:\Python\my_blog\MyBlog\photoes', height_field=None, width_field=None, max_length=100)