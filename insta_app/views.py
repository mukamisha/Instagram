from django.shortcuts import render
from django.http  import HttpResponse
from . models import Image
from django.contrib.auth.decorators import login_required.
# Create your views here.


@login_required(login_url='/accounts/login/')
def images(request):
    image= Image.objects.all()
    return render(request, 'home.html',{'images':image})
