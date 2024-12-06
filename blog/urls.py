from django.urls import path
import blog.views as blog_views


urlpatterns = [
    path("", blog_views.post_show, name="post_show" )
]