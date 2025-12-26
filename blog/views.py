from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, "blog/index.html", {'posts': posts})  # Added 'blog/' prefix

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_post.html', {'form': form})  # Added 'blog/' prefix

def view_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/view_post.html', {'post': post})  # Added 'blog/' prefix

def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_post', pk=post.pk)  # redirect to view_post with pk
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('index')
