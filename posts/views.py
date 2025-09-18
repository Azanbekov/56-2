from django.shortcuts import render , HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm2, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def task_view(request):
    return HttpResponse("task view is working! ")

def html_view(request):
    if request.method == "GET":
        return render(request, 'base.html')

@login_required(login_url="/login/")
def post_list_view(request):
    posts = Post.objects.all()
    limit = 3
    if request.method == "GET":
        search = request.GET.get("search")
        category_id =request.GET.get("search")
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page", 1))
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search) )
        if category_id:
            posts = posts.filter(category_id=category_id)
        if ordering:
            posts = posts.order_by(ordering)
        if page:
            max_pages = posts.count() // limit
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1
            elif round(max_pages) > max_pages:
                max_pages = round(max_pages)
            start = (page - 1) * limit
            end = page * limit           
            posts = posts[start:end]

        
        form = SearchForm()
        return render (request, "posts/post_list.html", context={"posts_list": posts, "form": form, "max_pages": range(1, max_pages + 1)})

@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    if request.method =="GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})

@login_required(login_url="/login/")    
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