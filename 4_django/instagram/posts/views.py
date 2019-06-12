from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
        return redirect("posts:index")
    else:
        form = PostForm()
        context = {
            'form':form
        }
        return render(request, 'posts/create.html', context)