from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from . import forms

#def home_view(request):
#    return render(request, 'home.html')

def signup_view(request):
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('hero:index')
    return render(request, 'registration/signup.html', {'form': form})
