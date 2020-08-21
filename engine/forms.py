from django import forms

from .models import Category, Item


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'category', 'text', 'image')


class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'category', 'text', 'image')
