from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.core import serializers





def index(request):
    posts = StoryPost.objects.all()
    return render(request, 'index.html', {'posts' : posts})



def add(request):
    print(request)
    if request.method == 'POST':
        author = request.POST['author-field'].capitalize()
        content = request.POST['content-field']
        post = StoryPost(author=author, content=content)
        post.save()
        return redirect('highlight')

    return render(request, 'add.html')
    


def highlight(request):
    posts = StoryPost.objects.all()
    highlight = posts.last()
    data = StoryPost.objects.exclude(id=highlight.id)
    return render(request, 'index.html', {'posts' : data, 'highlight' : highlight})
    

def entry(request, id):
    post = [StoryPost.objects.get(id=id)]
    post_json = serializers.serialize('json', post)
    return JsonResponse({'data': post_json})