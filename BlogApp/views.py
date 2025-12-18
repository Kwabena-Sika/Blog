from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import BlogTopic, BlogEntry
from . forms import BlogForm, BlogEntriesForm
from django.http import Http404
# Create your views here.
def index(request):
  return render(request, 'BlogApp/index.html')

@login_required
def blog_topics(request):
  topics = BlogTopic.objects.filter(owner=request.user).order_by('date_created')
  context = {'topics': topics}
  return render(request, 'BlogApp/topics.html', context)

@login_required
def add_topic(request):
  if request.method != "POST":
    form = BlogForm()
  else:
    form = BlogForm(data=request.POST)
    if form.is_valid():
      new_topic = form.save(commit=False)
      new_topic.owner = request.user
      new_topic.save()
      form.save()
      return redirect('BlogApp:blog_topics')
  context = {'form':form}
  return render(request, 'BlogApp/add_topic.html', context)

@login_required
def blog_entry(request, title_id):
  title = BlogTopic.objects.get(id=title_id)
  if title.owner != request.user:
    raise Http404
  posts = title.blogentry_set.order_by('-date_created')
  context = {'title':title, 'posts': posts}
  return render(request, 'BlogApp/blog_entry.html', context)

@login_required
def add_post(request, title_id):
  title = BlogTopic.objects.get(id=title_id)
  if request.method != "POST":
    form = BlogEntriesForm()
  else:
    form = BlogEntriesForm(data=request.POST)
    if form.is_valid():
      new_entry = form.save(commit=False)
      new_entry.title = title
      new_entry.save()
      return redirect('BlogApp:blog_entry', title_id=title_id)
  
  context = {'form':form, 'title':title}
  return render(request,'BlogApp/add_blog.html', context)

@login_required
def edit_post(request, post_id):
  post= BlogEntry.objects.get(id=post_id)
  title = post.title
  # if title.owner != request.user:
  #   raise Http404
  if request.method != "POST":
    form = BlogEntriesForm(instance=post)
  else:
    form = BlogEntriesForm(instance=post, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('BlogApp:blog_entry', title_id=title.id)
  context = {'post': post, 'title':title, 'form':form}
  return render(request, 'BlogApp/edit_post.html', context)