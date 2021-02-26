from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

#def home_view(request):
#    return render(request, 'home.html')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('hero:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
