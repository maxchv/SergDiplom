from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .forms import UserFormView
from gallery.models import Photo, HeadImage
from orders.models import FeedBack
from random import shuffle


def landing(request):
    #form_client = ClientForm(request.POST or None)
    photos = list(Photo.objects.all())
    shuffle(photos)
    comments = list(FeedBack.objects.filter(checked=True))
    shuffle(comments)
    head_images = HeadImage.objects.all()
    # if request.method == "POST" and form_client.is_valid():
    #     data = form_client.cleaned_data
    #     new_form = form_client.save()
    login_form = AuthenticationForm()
    register_form = UserFormView()
    context = {#"form_client": form_client,
               "login_form": login_form,
               'register_form': register_form,
               'head_images': head_images,
               'photos': photos[:8],
               "comments": comments[:5]}
    return render(request, 'landing/index.html', context)


def registration(request):
    return render(request, 'registration/login.html')


