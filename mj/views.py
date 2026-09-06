#from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse  
from django.shortcuts import render, redirect    
from mj.bot import get_bot_response
from mj.forms import EmployeeForm    
from mj.models import Employee    

def home(request):
    return render(request, "index.html")

def createEmp(request):     
    if request.method == "POST":    
        form = EmployeeForm(request.POST)    
        if form.is_valid():    
            form.save()    
            return redirect('/show')    
    else:    
        form = EmployeeForm()    
    return render(request, 'index.html', {'form': form})    
def show(request):    
    employees = Employee.objects.all()    
    return render(request, "show.html", {'employees': employees})    
def edit(request, id):    
    employee = Employee.objects.get(id=id)    
    return render(request, 'edit.html', {'employee': employee})    
def update(request, id):    
    employee = Employee.objects.get(id=id)    
    form = EmployeeForm(request.POST, instance=employee)    
    if form.is_valid():    
        form.save()    
        return redirect("/show")    
    return render(request, 'edit.html', {'employee': employee})    
def destroy(request, id):    
    employee = Employee.objects.get(id=id)    
    employee.delete()    
    return redirect("/show")  

from django.shortcuts import render, get_object_or_404, redirect  
from .forms import UploadFileForm  
from .models import UploadedFile  
import os  
from django.conf import settings  
# Upload and list files  
def upload_file(request):  
    if request.method == 'POST':  
        form = UploadFileForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'File uploaded successfully!')
            return redirect('upload_file')  
    else:  
        form = UploadFileForm()  
    files = UploadedFile.objects.all()  
    return render(request, 'file_upload/uploadform.html', {'form': form, 'files': files})
# Delete file (with confirmation)  
def delete_file(request, file_id):  
    file = get_object_or_404(UploadedFile, id=file_id)  
    if request.method == 'POST':  
        file_path = file.file.path  # absolute path to file  
        file.delete()  # delete from database  
        if os.path.exists(file_path):  
            os.remove(file_path)  # remove file from folder  
        return redirect('upload_file')  
    return render(request, 'file_upload/confirm_delete.html', {'file': file})
from django.shortcuts import render
from .bot import get_bot_response


def chat(request):

    response = ""

    if request.method == "POST":

        user_message = request.POST.get("message", "")

        if user_message.strip():
            response = get_bot_response(user_message)

    return render(request, "bot.html", {
        "response": response
    })