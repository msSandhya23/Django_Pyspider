from django import forms
class StudentForm(forms.Form):
    StName = forms.CharField()
    StAge = forms.IntegerField()
    #Address = forms.CharField(widget=forms.Textarea)
    Password = forms.CharField(widget=forms.PasswordInput)
    