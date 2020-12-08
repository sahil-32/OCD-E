from django.shortcuts import render,redirect
from .forms import CompilerForm
import time
import sys
import subprocess
from subprocess import Popen, PIPE
from user.models import Document
from django.core.files import File
# Create your views here.
primarykey=0
isedit = False
lang = 1

def home(request):
    return render(request, 'mainapp/home.html')

def edit(request,pk):
    global primarykey
    global isedit
    primarykey = pk
    isedit = True
    file = Document.objects.get(pk=pk)
    pth = file.docfile.path
    with open(pth) as f:
        with open("myfile.txt", "w") as f1:
            for line in f:
                f1.write(line)
    return redirect('compiler')


def compiler(request):
    global lang
    if request.method == 'POST':
        form = CompilerForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            input = form.cleaned_data['input']
            language = int(form.cleaned_data['language'])
            lang = language
            file1 = open("input.txt","w") 
            file1.writelines(str(input)) 
            file1.close()

            if(language ==1):
                file1 = open("myfile.cpp","w") 
                file1.writelines(str(code)) 
                file1.close()

                file1 = open("myfile.txt","w") 
                file1.writelines(str(code)) 
                file1.close()

                txt1 = "g++ myfile.cpp"
                txt2 = "./a.out < input.txt"
                command1 = [txt1]
                command2 = [txt2]
                p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p.wait()
                text,err = p.communicate()
                file1 = open("out.txt","w") 
                if(p.returncode !=0):
                    file1.writelines(str(err.decode('utf-8')))
                else:
                    q = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    text2,err2 = q.communicate()
                    if(q.returncode !=0):
                        file1.writelines(str(err2.decode('utf-8')))
                    else:
                        file1.writelines(str(text2.decode('utf-8')))
                file1.close()
                return redirect('output')
            elif(language==2):
                file1 = open("myfile.py","w") 
                file1.writelines(str(code)) 
                file1.close()

                file1 = open("myfile.txt","w") 
                file1.writelines(str(code)) 
                file1.close()

                txt1 = "python3 myfile.py < input.txt"
                command1 = [txt1]
                p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p.wait()
                text,err = p.communicate()
                file1 = open("out.txt","w") 
                if(p.returncode !=0):
                    err2 = err.decode('utf-8')
                    file1.writelines(str(err2))
                else:
                    file1.writelines(str(text.decode('utf-8')))
                file1.close()

                return redirect('output')

            else:
                file1 = open("myfile.java","w") 
                file1.writelines(str(code)) 
                file1.close()

                file1 = open("myfile.txt","w") 
                file1.writelines(str(code)) 
                file1.close()

                txt1 = "java myfile.java < input.txt"
                command1 = [txt1]
                p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p.wait()
                text,err = p.communicate()
                file1 = open("out.txt","w") 
                if(p.returncode !=0):
                    err2 = err.decode('utf-8')
                    file1.writelines(str(err2))
                else:
                    file1.writelines(str(text.decode('utf-8')))
                file1.close()

                return redirect('output')
    else:
        with open('myfile.txt','r') as file:
            codestr = file.read()
        form = CompilerForm(initial={'code': codestr})
    return render(request, 'mainapp/compiler.html', {'form': form})

def output(request): 
    global primarykey
    global isedit
    if(isedit):
        if request.method == 'POST':
            file = Document.objects.get(pk=primarykey)
            pth = file.docfile.path
            with open(pth,"w") as f:
                with open("myfile.txt", "r") as f1:
                    for line in f1:
                        f.write(line)
            return redirect('compiler')

        else:
            f8 = open("out.txt","r")
            file_content = f8.read()
            f8.close()
            context = {'file_content': file_content,'isedit':isedit}
            return render(request, "mainapp/output.html", context) 
    else:
        if request.method == 'POST':
            global lang
            name = request.POST.get('name')
            count = Document.objects.filter(user=request.user).count()
            if(count == 10):
                return redirect('failure')
            else:
                if(lang == 1):
                    local_file = open('myfile.cpp')
                    djangofile = File(local_file)
                    d = Document(name=name,docfile=djangofile,user=request.user)
                    d.docfile.name = name
                    d.save()
                    return redirect('compiler')
                elif(lang == 2):
                    local_file = open('myfile.py')
                    djangofile = File(local_file)
                    d = Document(name=name,docfile=djangofile,user=request.user)
                    d.docfile.name = name
                    d.save()
                    return redirect('compiler')
                elif(lang == 3):
                    local_file = open('myfile.java')
                    djangofile = File(local_file)
                    d = Document(name=name,docfile=djangofile,user=request.user)
                    d.docfile.name = name
                    d.save()
                    return redirect('compiler')
        else:
            f8 = open("out.txt","r")
            file_content = f8.read()
            f8.close()
            context = {'file_content': file_content,'isedit':isedit}
            return render(request, "mainapp/output.html", context)     
    
def reset(request):
    global isedit
    isedit = False
    open('myfile.txt', 'w').close()
    return redirect('homepage')