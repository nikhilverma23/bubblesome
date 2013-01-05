from django import forms

class UploadImageForm(forms.Form):
    """
    """
    title =  forms.CharField(max_length=100,initial="Title of Image")
    image = forms.ImageField(required=False)