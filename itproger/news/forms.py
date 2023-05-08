from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anouns', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title'
            }),

            'anouns': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article anouns'
            }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publish date'
            })
        }