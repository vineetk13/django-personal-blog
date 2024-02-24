from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login

from users.forms import CustomUserCreationForm

def user_register(request):
    context = {
        "form": CustomUserCreationForm
    }
    print(request.path)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse("blog_index"))
        else:
            return render(request, 'users/register.html', context)
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("blog_index"))