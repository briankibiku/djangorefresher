from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Learn py",
        "author": "Abdi"
    },
    {
        "id": 2,
        "title": "Learn ANgular",
        "author": "jalem"
    },
    {
        "id": 3,
        "title": "Learn javascript",
        "author": "Kebisis"
    }
]


def index(request: HttpRequest):
    name = request.GET.get('name') or "Unanymouse"
    context = {
        "name": name,
        "posts": posts,
        "title": 'All Posts'
    }

    return render(request, 'index.html', context)


def about(request):
    context = {
        "title": 'About Posts'
    }
    return render(request, 'about.html', context)


def services(request):
    context = {
        "title": 'Services Posts'
    }
    return render(request, 'services.html', context)


def greet(request: HttpRequest):
    name = request.GET.get('name') or "Unanymouse"

    return HttpResponse(f"Hello {name}")


def all_posts(request: HttpRequest):
    return HttpResponse(str(posts))


def single_post(requst: HttpRequest, post_id):
    for post in posts:
        if post['id'] == post_id:
            return HttpResponse(str(post))
    return HttpResponse('Not Found')
