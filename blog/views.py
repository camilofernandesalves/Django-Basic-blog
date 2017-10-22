from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Post

# Create your views here.

def home(request):

    name = "Camilo"
    # categories = ['PHP', 'Java', 'Ruby']
    # for category in categories:
        # Category.objects.create(name=category)

    all_categories = Category.objects.all()
    category = Category.objects.get(name='Ruby')
    posts = Post.objects.filter(status="Published")
    # Para todos Post.objects.all()

    # post = Post()
    # post.name = "Show post 3"
    # post.content = "Content of my  post"
    # post.status = "Published"
    # post.category = category

    # post.save()

    context = {
        'name': name,
        'categories': all_categories,
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)
