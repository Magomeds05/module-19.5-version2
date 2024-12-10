from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from postapp.models import Post


def post_add(request):
    page1 = request.GET.get('per_page') or 2
    posts = Post.objects.all().order_by('-id') or page1
    paginator = Paginator(posts, page1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'posting.html', context=posts)
# Create your views here.
