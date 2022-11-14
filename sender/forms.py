from django import forms
from ckeditor.fields import RichTextField
class SenderForm(forms.Form):
    theme = forms.CharField(label="Enter theme ...", max_length=100)
    email  = forms.EmailField(label="Enter email...")
    message = RichTextField()
    