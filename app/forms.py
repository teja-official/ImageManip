from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
  image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
  class Meta:
    model = Image
    fields = ('image', )

