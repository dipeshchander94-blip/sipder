from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from mj.bot import get_bot_response
from mj.forms import EmployeeForm, UploadFileForm
from mj.models import Employee, UploadedFile

import os


# =========================
# HOME
# =========================

def home(request):
    return render(request, "index.html")


# =========================
# ADD EMPLOYEE
# Visitor bhi employee add kar sakta hai
# =========================

def createEmp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = EmployeeForm()

    return render(request, 'index.html', {'form': form})


# =========================
# SHOW EMPLOYEE RECORDS
# Sirf logged-in user
# =========================

@login_required
def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


# =========================
# EDIT EMPLOYEE
# Sirf logged-in user
# =========================

@login_required
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


# =========================
# UPDATE EMPLOYEE
# Sirf logged-in user
# =========================

@login_required
def update(request, id):
    employee = Employee.objects.get(id=id)

    form = EmployeeForm(request.POST, instance=employee)

    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(
        request,
        'edit.html',
        {
            'employee': employee,
            'form': form
        }
    )


# =========================
# DELETE EMPLOYEE
# Sirf logged-in user
# =========================

@login_required
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect("/show")


# =========================
# FILE UPLOAD
# =========================

def upload_file(request):

    if request.method == 'POST':

        form = UploadFileForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'File uploaded successfully!'
            )

            return redirect('upload_file')

    else:
        form = UploadFileForm()

    files = UploadedFile.objects.all()

    return render(
        request,
        'file_upload/uploadform.html',
        {
            'form': form,
            'files': files
        }
    )


# =========================
# DELETE FILE
# =========================

def delete_file(request, file_id):

    file = get_object_or_404(
        UploadedFile,
        id=file_id
    )

    if request.method == 'POST':

        file_path = file.file.path

        file.delete()

        if os.path.exists(file_path):
            os.remove(file_path)

        return redirect('upload_file')

    return render(
        request,
        'file_upload/confirm_delete.html',
        {
            'file': file
        }
    )


# =========================
# AI CHATBOT
# =========================

def chat(request):

    response = ""

    if request.method == "POST":

        user_message = request.POST.get(
            "message",
            ""
        )

        if user_message.strip():
            response = get_bot_response(
                user_message
            )

    return render(
        request,
        "bot.html",
        {
            "response": response
        }
    )