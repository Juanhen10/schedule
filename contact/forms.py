from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactFrom(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe a classe b',
                'placeholder': 'escreva aqui'
            }

        ),
        label='Primeiro nome',
        help_text='Texto de ajuda',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classes-a classe-b',
        #     'placeholder': 'Escreva aqui',
        # })

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone')
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'})

        # }

    def clean(self):
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='ivalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError('Mensagem de erro 2', code='invalid')
        )

        return super().clean()
