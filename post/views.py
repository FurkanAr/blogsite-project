from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from django.db.models import Q
from .forms import PostForm
from django.contrib import messages
from django.urls import reverse_lazy


def post_list(request):
    posts = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(posts, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts,
    }
    return render(request, 'blog.html', context )

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,

    }
    return render(request, 'article.html', context)

def post_create(request):

    if not request.user.is_authenticated:
        return Http404()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Post was created successfully')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form' : form,
    }

    return render(request, 'form.html', context )

def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance = post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post was updated successfully')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form' : form,
    }
    return render(request, 'form.html', context )


def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post was deleted successfully')

    return redirect("post_list")