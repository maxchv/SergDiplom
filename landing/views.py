from django.shortcuts import render
from .forms import ClientForm
from gallery.models import Photo

#@login_required
def landing(request):
    form_client = ClientForm(request.POST or None)
    photos = Photo.objects.all()[:6]
    if request.method == "POST" and form_client.is_valid():
        print(request.POST)
        print(form_client.cleaned_data)
        data = form_client.cleaned_data

        print(form_client.cleaned_data["first_name"])
        print(data["first_name"])
        new_form = form_client.save()
    return render(request, 'landing/index.html', {"form_client": form_client, 'photos': photos})

def registration(request):
    return render(request, 'registration/login.html')


