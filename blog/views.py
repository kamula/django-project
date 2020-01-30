from django.shortcuts import render

# Create your views here.

post = [
    {
        'author': 'isaac',
        'title': 'blog 1',
        "content": "first blog content",
        'date': '23 January 2020'
    },
    {
        'author': 'Florence',
        'title': 'blog 2',
        "content": "second blog content",
        'date': '24 January 2020'
    }
]


def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
