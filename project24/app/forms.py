from django import forms
class StudentForm(forms.Form):
    StName = forms.CharField(max_length=100)
    StAge = forms.IntegerField()
    Address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}))
    Password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[('MALE','Male'),('FEMALE','female')],widget=forms.RadioSelect)
    