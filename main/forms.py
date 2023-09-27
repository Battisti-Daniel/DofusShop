from django import forms
from account.models import Item


class MyFloatInput(forms.TextInput):
    input_type = 'text'


class ItemModelForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('value', 'server', 'cover', 'gear')

        # remove arrow integer field
        widgets = {
            'value': MyFloatInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # remove first field because = -------
        self.fields['server'].widget.choices = [(value, label) for value, label in self.fields['server'].widget.choices
                                                if value]

        # remove first field because = -------
        self.fields['gear'].widget.choices = [(value, label) for value, label in self.fields['gear'].widget.choices
                                              if value]


class ItemModelCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'value', 'gear', 'server', 'cover')

        # remove arrow integer field
        widgets = {
            'value': MyFloatInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # remove first field because = -------
        self.fields['server'].widget.choices = [(value, label) for value, label in self.fields['server'].widget.choices
                                                if value]

        # remove first field because = -------
        self.fields['gear'].widget.choices = [(value, label) for value, label in self.fields['gear'].widget.choices
                                              if value]
