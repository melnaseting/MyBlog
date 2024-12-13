from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author , Comment
from blog.forms import CommentForm

# Create your views here.
def post_show(request):
    posts = Post.objects.all()
    coments = Comment.objects.all()
    form = CommentForm()
    
    if request.method == 'POST':
        if 'sub_btn' in request.POST :
            form = CommentForm(request.POST)
            pk = request.POST.get('sub_btn')
            
            form.save()

    context = {
        "posts": posts,
        "comment":coments,
        "form": form,
        }

    return render(
        request,
        "blog/post.html",
        context = context,
    )

def author_show(request , id):
    authors = Author.objects.all()
    for i in authors:
        if i.id == id:
            author = authors[id-1]

    posts = Post.objects.all()
    context = {
        "author": author,
        "posts": posts,
        }

    return render(
        request,
        "blog/author.html",
        context = context,
    )

def basic_page(request):
    return render(
        request,
        "blog/basic.html",
    )