from django import forms
from account.models import Item


class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('value', 'server')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['server'].widget.choices = [(value, label) for value, label in self.fields['server'].widget.choices
                                                if value]


class MyFloatInput(forms.TextInput):
    input_type = 'text'


class ItemModelCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'value', 'gear', 'server', 'cover')

        widgets = {
            'value': MyFloatInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['server'].widget.choices = [(value, label) for value, label in self.fields['server'].widget.choices
                                                if value]


