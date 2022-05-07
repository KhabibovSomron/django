from dataclasses import fields
from pyexpat import model
from statistics import mode
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent"})
        }