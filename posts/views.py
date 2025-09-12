from django.shortcuts import render , HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm2

# Create your views here.
def task_view(request):
    return HttpResponse("task view is working! ")

def html_view(request):
    if request.method == "GET":
        return render(request, 'base.html')

def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render (request, "posts/post_list.html", context={"posts_list": posts})

def post_detail_view(request, post_id):
    if request.method =="GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})
    
def post_create_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render (request, "posts/post_create.html", context={"form": form})
    if request.method =="POST":   
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            form.save()
            # title = cleaned_data.get ("title")
            # content = cleaned_data.get("content")
            # image = cleaned_data.get("image")
            post = Post.objects.create(title=title, content=content, image=image)
            return redirect("/")