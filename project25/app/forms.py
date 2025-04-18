from django import forms
from app.models import *

# Create your forms here.
class SchoolForm(forms.Form):
    Scname = forms.CharField()
    ScLocation = forms.CharField()
    #ScPrinciple = forms.CharField()
class StudentForm(forms.Form):
    Scname = forms.ModelChoiceField(queryset=School.objects.all())
    StName = forms.CharField()
    StAge = forms.ImageField()
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 5}))
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices = [('MALE','Male')],widget=forms.RadioSelect)
    
    