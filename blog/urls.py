from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.post_show, name="post_show" ),
    path("author/<int:id>",blog_views.author_show , name="author_show")
]