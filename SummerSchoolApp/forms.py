from django import forms
import datetime


class FileFieldForm(forms.Form):
    year = forms.IntegerField(default=datetime.datetime.now().year)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
