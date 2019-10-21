from django.shortcuts import render
from django.http  import HttpResponse
from . models import Image
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def images(request,):
    image= Image.objects.all()
    return render(request, 'home.html',{'images':image})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('image')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
