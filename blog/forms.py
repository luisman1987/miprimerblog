from django import forms
from .models import Postear

class PostForm(forms.ModelForm):

    class Meta:
        model = Postear
        fields = ('titulo', 'texto',)
