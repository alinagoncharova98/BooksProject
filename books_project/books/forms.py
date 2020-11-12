from django.forms import ModelForm, TextInput
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'owner']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',

                'placeholder': 'Enter name',
            }),

            'owner': TextInput(attrs={
                'class': 'form-control',

                'placeholder': 'Enter owner',
            })
        }

