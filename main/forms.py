from django import forms
from account.models import Item


class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('value', 'characteristics', 'server')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['server'].widget.choices = [(value, label) for value, label in self.fields['server'].widget.choices
                                                if value]
        self.fields['characteristics'].widget.choices = [(value, label) for value, label in
                                                         self.fields['characteristics'].widget.choices if value]


class ItemModelCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'value', 'characteristics', 'server', 'cover')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['server'].widget.choices = [(value, label) for value, label in self.fields['server'].widget.choices
                                                if value]
        self.fields['characteristics'].widget.choices = [(value, label) for value, label in
                                                         self.fields['characteristics'].widget.choices if value]

