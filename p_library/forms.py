from django import forms
from django.forms import formset_factory

from .models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


AuthorFormSet = formset_factory(AuthorForm, extra=4)

author_formset = AuthorFormSet()
