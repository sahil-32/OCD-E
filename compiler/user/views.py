from django.shortcuts import render, redirect
from .forms import UserRegisterForm
import sys
import subprocess
from subprocess import Popen, PIPE

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            txt1 = "mkdir ../storage/{}".format(username)
            command1 = [txt1]
            p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})