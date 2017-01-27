from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

@login_required
def gallery(request):
    if not request.user.is_superuser:
        return redirect("landing")
    photos = Photo.objects.all()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, "gallery/index.html", {"photos": photos, "form": form})
    form = PhotoForm()
    return render(request, "gallery/index.html", {"photos": photos, "form": form})




