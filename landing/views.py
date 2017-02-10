from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render
from .forms import UserFormView
from gallery.models import Photo, HeadImage
from orders.models import FeedBack
from random import shuffle


def landing(request):
    # form_client = ClientForm(request.POST or None)
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
    context = {  # "form_client": form_client,
        "login_form": login_form,
        'register_form': register_form,
        'head_images': head_images,
        'photos': photos[:8],
        "comments": comments[:5]}
    return render(request, 'landing/index.html', context)


def registration(request):
    return render(request, 'registration/login.html')


def login_ajax(request):
    if request.is_ajax:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                login_form.clean()
                user = login_form.get_user()
                login(request, user)
                if user.is_superuser:
                    return JsonResponse({'status': 'ok',
                                         'welcome': user.username,
                                         'menu': [
                                             {'title': 'Админ панель',
                                              'link': '/admin'
                                              }
                                         ],
                                         'error': ''})
            else:
                return JsonResponse({'status': 'user is not valid'})
        return JsonResponse({'status': 'it should be only post request'})
    return JsonResponse({'status': 'it is not ajax request'})
