from django.db import models
from django import forms
from django.shortcuts import redirect
from django.utils.timezone import now
from datetime import timedelta
import sqlite3

# Create your models here.

conn = sqlite3.connect("MyBlog\db.sqlite3")
cursor = conn.cursor()

class Author(models.Model):
    name = models.CharField(max_length=15)
    bio = models.TextField(null=True, blank=True)
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return self.text


class Post(models.Model):
    def published_recently(self):
        return now()- self.published_date <= timedelta(days=7)
    
    title = models.CharField(max_length=15)
    content = models.TextField(blank=True , null=False)
    published_date = models.DateTimeField()
    photo = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ManyToManyField(Comment)

    def __str__(self) -> str:
        return f"{self.title} , {self.published_date}"
    
    def add_comment(post_id, author , comment_text):
        cursor.execute(f"INSERT INTO blog_coment (author, text) VALUES ({author}, {comment_text})")
        cursor.execute("SELECT * FROM blog_coment WHERE id=(SELECT max(id) FROM blog_coment)")
        result = cursor.fetchall()
        for el in result :
            for i in el:
                coment_id = i
        cursor.execute(f"INSERT INTO blog_post_coment (post_id, comment_id) VALUES ({post_id}, {coment_id})")
        conn.commit()
    
    
   




    