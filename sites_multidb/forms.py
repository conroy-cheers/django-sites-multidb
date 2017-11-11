from django import forms
from .models import DBConfig


class DBConfigForm(forms.ModelForm):
    class Meta:
        model = DBConfig
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }
