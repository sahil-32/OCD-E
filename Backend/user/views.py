from django.shortcuts import render, redirect
from .forms import UserRegisterForm,DocumentForm
import sys
import subprocess
from subprocess import Popen, PIPE
from django.core.files.storage import FileSystemStorage
from .models import Document

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

def get(request):
    documents_list = Document.objects.filter(user=request.user)
    return render(request, 'user/viewfile.html', {'documents': documents_list})

def post(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'],user=request.user,name=form.cleaned_data['name'])
            newdoc.docfile.name = form.cleaned_data['name']
            newdoc.save()
            return redirect('viewfile')
    else:
        form = DocumentForm() 

    return render(request, 'user/upload.html', {'form': form})

def delete(request,pk):
    if request.method == 'POST':
        file = Document.objects.get(pk=pk)
        file.delete()
    return redirect('viewfile')