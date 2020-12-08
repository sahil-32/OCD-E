from django.shortcuts import render,redirect
from .forms import CompilerForm
import time
import sys
import subprocess
from subprocess import Popen, PIPE

# Create your views here.

def home(request):
    return render(request, 'mainapp/home.html')

def compiler(request):
    if request.method == 'POST':
        form = CompilerForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            input = form.cleaned_data['input']
            language = int(form.cleaned_data['language'])

            file1 = open("input.txt","w") 
            file1.writelines(str(input)) 
            file1.close()

            if(language ==1):
                file1 = open("myfile.cpp","w") 
                file1.writelines(str(code)) 
                file1.close()

                txt1 = "g++ myfile.cpp"
                txt2 = "./a.out < input.txt"
                command1 = [txt1]
                command2 = [txt2]
                p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(2)
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
                txt1 = "python3 myfile.py < input.txt"
                command1 = [txt1]
                p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(2)
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
                txt1 = "java myfile.java < input.txt"
                command1 = [txt1]
                p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(2)
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
        form = CompilerForm()
    return render(request, 'mainapp/compiler.html', {'form': form})

def output(request): 
    f = open("out.txt","r")
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    
    return render(request, "mainapp/output.html", context) 