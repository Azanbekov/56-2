from django.shortcuts import render , HttpResponse
from posts.models import Post

# Create your views here.
def task_view(request):
    return HttpResponse("task view is working! ")

def html_view(request):
    return render(request, 'base.html')

def post_list_view(request):
    posts = Post.objects.all()
    return render (request, "posts/post_list.html", context={"posts_list": posts})