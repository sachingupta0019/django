from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import ImageUploaderForm
from .models import ImgBoxDB

# Create your views here.
def index(request):
    if request.method == "POST":
        ImgBoxForm = ImageUploaderForm(request.POST, request.FILES)
        if ImgBoxForm.is_valid():
            ImgBoxForm.save()
    ImgBoxForm = ImageUploaderForm()
    img = ImgBoxDB.objects.all()
    return render(request, "ImgBox/index.html/",  {"ImgForm" : ImgBoxForm, 'img' : img})

def deleteImage(request, id):
    if request.method == "POST":
        img = ImgBoxDB.objects.get(pk = id)
        img.delete()
        return HttpResponseRedirect('/home/')
    return HttpResponse("Error")
