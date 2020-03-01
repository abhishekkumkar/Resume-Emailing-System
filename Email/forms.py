from django import forms

class EmailForm(forms.Form):
    email               = forms.EmailField(widget = forms.EmailInput(attrs = {"class":"form-control", "placeholder":"Enter email" }))

class QRForm(forms.Form):
    Name               = forms.CharField(max_length=120,widget = forms.TextInput(attrs = {"class":"form-control","placeholder":"Enter Name"}))

    # File               =  forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))


