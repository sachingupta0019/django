from django.shortcuts import render, get_list_or_404, HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
# Create your views here.
def index(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data
            form.save()
        candidate = Resume.objects.all()
        return render(request, 'index.html/', {'candidate': candidate})
    else:
        form = ResumeForm(label_suffix="")
        candidate = Resume.objects.all()
        return render(request, 'index.html/', {'form' : form, 'candidate': candidate})
    
def user_profile(request, id = None):
    user = get_list_or_404(Resume, pk = id)
    return render(request, 'user-profile.html/', {'user': user})

def profile_update(request, id):
    if request.method == "POST":
        update_profile = Resume.objects.get(pk = id)
        update_form = ResumeForm(request.POST, request.FILES, instance=update_profile)
        if update_form.is_valid():
            update_form.cleaned_data
            update_form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'profile-edit.html/', {'update_form' : update_form, 'id' : id})
    else:
        update_profile = Resume.objects.get( pk = id)
        update_form = ResumeForm(instance=update_profile)
        return render(request, 'profile-edit.html/', {'update_form' : update_form, 'id' : id})