from django.shortcuts import render
from .forms import ClientForm
from  django.utils.timezone import now
from django.contrib.auth.decorators import login_required

#@login_required
def landing(request):
    form = ClientForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data

        print(form.cleaned_data["first_name"])
        print(data["first_name"])
        new_form = form.save()
    return render(request, 'landing/index.html', locals())

def registration(request):
    return render(request, 'registration/login.html')


