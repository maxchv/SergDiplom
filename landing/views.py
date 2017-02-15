from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorDict, ErrorList
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import render
from .forms import UserFormView
from .models import ClientProfile
from gallery.models import Photo, HeadImage
from orders.models import FeedBack
from orders.forms import OrderForm
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
    context = {  # "form_client": form_client,
        "login_form": AuthenticationForm(),
        'register_form': UserFormView(),
        'order_form': OrderForm(),
        'head_images': head_images,
        'photos': photos[:8],
        "comments": comments[:5]}
    return render(request, 'landing/index.html', context)


def registration(request):
    return render(request, 'registration/login.html')


def registration_ajax(request):
    if request.is_ajax:
        if request.method == 'POST':
            form = UserFormView(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                #username = form.cleaned_data.get('username')
                #password = form.cleaned_data.get('password1')
                #print('user: {} password: {}'.format(username, password))
                #print(user.username, user.password, user.is_superuser)
                try:
                    user.save()
                    client = ClientProfile.objects.create(user=user)
                    client.save()
                except Exception as ex:
                    return JsonResponse({'status': 'exception',
                                         'message': ex})
                return JsonResponse({'status': 'ok',
                                     'user': client.user.username,
                                     'message': 'welcome'})
            else:
                error_message = [v.get_json_data() if v and isinstance(v, ErrorList) else v for k, v in
                                 form.errors.items()]
                return JsonResponse({'status': 'error',
                                     'user': 'nobody',
                                     'message': error_message})
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def login_ajax(request):
    if request.is_ajax:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                form.clean()
                user = form.get_user()
                login(request, user)
                if user.is_superuser:
                    return JsonResponse({'status': 'ok',
                                         'user': user.username,
                                         'menu': [
                                             {
                                                 'title': 'Админ панель',
                                                 'link': '/admin',
                                                 'id': 'btn-admin-panel'
                                             }
                                         ],
                                         'message': 'welcome superuser'})
                else:
                    return JsonResponse({'status': 'ok',
                                         'user': user.username,
                                         'menu': [
                                             {
                                                 'title': 'Мои заказы',
                                                 'link': '#',
                                                 'id': 'btn-orders'
                                             },
                                             {
                                                 'title': 'Мои отзывы',
                                                 'link': '#',
                                                 'id': 'btn-feedback'
                                             },
                                         ],
                                         'message': 'welcome client'})
            else:
                error_message = [v.get_json_data() if v and isinstance(v, ErrorList) else v for k, v in
                                 form.errors.items()]
                return JsonResponse({'status': 'error',
                                     'user': 'nobody',
                                     'menu': [],
                                     'message': error_message})
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
