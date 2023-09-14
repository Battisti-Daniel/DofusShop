from django import forms
from account.models import Item


class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('value', 'characteristics', 'server')

