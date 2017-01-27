from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.draft = True
            feedback.save()
            return redirect("orders")
    else:
        form = FeedBackForm()
    context = {"form": form}
    return render(request, "orders/index.html", context)