from django import forms


class employeeform(forms.Form):
    fname=forms.CharField(max_length=30)
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    address=forms.CharField(max_length=50)
    photo=forms.FileField()
    designation=forms.CharField(max_length=30)

