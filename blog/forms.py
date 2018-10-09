from django import forms

from .models import publicacion

class PostForm(forms.ModelForm):

    class Meta:
        model = publicacion
        fields = ('titulo', 'texto',)
