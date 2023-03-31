from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.core import serializers





def index(request):
    posts = Quote.objects.all()
    return render(request, 'index.html', {'posts' : posts})



def add(request):
    if request.method == 'POST':
        author = request.POST['author-field'].capitalize()
        content = request.POST['content-field']
        post = Quote(author=Author.objects.get(pk=author), content=content)
        post.save()
        return redirect('highlight')
    
    authors = Author.objects.all()
    return render(request, 'add.html', {'authors' : authors})
    


def highlight(request):
    posts = Quote.objects.all()
    highlight = posts.last()
    data = Quote.objects.exclude(id=highlight.id)
    return render(request, 'index.html', {'posts' : data, 'highlight' : highlight})
    

def entry(request, id):
    post = [Quote.objects.get(id=id)]
    post_json = serializers.serialize('json', post)
    return JsonResponse({'data': post_json})