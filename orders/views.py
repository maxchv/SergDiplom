from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import FeedBackForm, OrderForm
from .models import FeedBack, Order


@login_required
def index(request):
    feedbacks = FeedBack.objects.filter(user=request.user).order_by("-date")
    orders = Order.objects.filter(client=request.user).order_by("-timestamp")
    form = FeedBackForm()
    order_form = OrderForm()
    context = {"form_feedback": form, 'feedbacks': feedbacks,
               'form_order': order_form, 'orders': orders}
    return render(request, "orders/index.html", context)


@login_required
def feedback_ajax(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.draft = True
            feedback.save()
            return JsonResponse({'status': 'ok',
                                 'message': '<h3>Спасибо за отзыв</h3>'})
        else:
            print(form.errors)
            return JsonResponse({'status': 'error',
                                 'message': str(form.errors)})
    return redirect("landing")


@login_required
def order_ajax(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_data = form.save(commit=False)
            order_data.client = request.user
            order_data.save()
            return JsonResponse({'status': 'ok',
                                 'message': '<h3>Заказ добавлен</h3>'})
        else:
            print(form.errors)
            return JsonResponse({'status': 'error',
                                 'user': request.user.username,
                                 'message': str(form.errors)})
    return redirect("landing")
