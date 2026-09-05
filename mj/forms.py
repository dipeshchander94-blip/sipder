from django import forms    
from mj.models import Employee    
class EmployeeForm(forms.ModelForm):    
    class Meta:    
        model = Employee    
        fields = "__all__"  

from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'file']
    
  