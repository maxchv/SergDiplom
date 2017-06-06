from random import shuffle

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.forms.utils import ErrorList
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.shortcuts import render

from gallery.models import Photo, HeadImage
from orders.forms import OrderForm, FeedBackForm
from orders.models import FeedBack, Order
from .forms import UserFormView
from .models import ClientProfile, Address, Section


def landing(request):
    if request.is_ajax():
        return JsonResponse({'status': 'error',
                             'user': 'nobody',
                             'message': "Don't support ajax request"})
    photos = list(Photo.objects.all())
    shuffle(photos)
    comments = list(FeedBack.objects.filter(checked=True))
    shuffle(comments)
    head_images = HeadImage.objects.all()
    order_form = OrderForm()
    if request.user.is_authenticated():
        last = Order.objects.order_by('-timestamp').filter(client=request.user).filter(phone__isnull=False).first()
        if last:
            order_form = OrderForm(initial={'phone': last.phone})

    context = {
        'address': Address.objects.first(),
        'about': Section.objects.first(),
        "login_form": AuthenticationForm(),
        'register_form': UserFormView(),
        'order_form': order_form,
        'feedback_form': FeedBackForm(),
        'head_images': head_images,
        'photos': photos[:8],
        "comments": comments[:5]}
    return render(request, 'landing/index.html', context)


def registration_ajax(request):
    if request.is_ajax:
        if request.method == 'POST':
            form = UserFormView(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                try:
                    user.save()
                    client = ClientProfile.objects.create(user=user)
                    client.save()
                except Exception as ex:
                    return JsonResponse({'status': 'exception',
                                         'message': str(ex)})
                return JsonResponse({'status': 'ok',
                                     'message': 'Спасибо за регистрацию. Введите логин и пароль'})
            else:
                return JsonResponse({'status': 'error',
                                     'message': str(form.errors)})
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
                                         'menu': [
                                             {
                                                 'title': 'Админ панель',
                                                 'link': '/admin',
                                                 'id': 'btn-admin-panel',
                                                 'target': ''
                                             }
                                         ],
                                         'message': 'welcome superuser'})
                else:
                    return JsonResponse({'status': 'ok',
                                         'menu': [
                                             {
                                                 'title': 'Мои заказы',
                                                 'link': '#',
                                                 'id': 'btn-orders',
                                                 'target': '#dlg-order'
                                             },
                                             {
                                                 'title': 'Мои отзывы',
                                                 'link': '#',
                                                 'id': 'btn-feedback',
                                                 'target': '#dlg-feedback'
                                             },
                                         ],
                                         'message': 'Добро пожаловать'})
            else:
                return JsonResponse({'status': 'error',
                                     'message': str(form.errors)})
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
