from django.shortcuts import render , HttpResponse

# Create your views here.
def website_view(request):
    return HttpResponse("website view is working! ")

def html_view(request):
    return render(request, 'base.html')