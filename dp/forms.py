from django import forms
from .models import Author, Book
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels = {'name': 'Author'}

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'u-full-width'}))


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']
        labels = {'name': 'Book'}

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'u-full-width'}))

BookFormset = inlineformset_factory(Author, Book, extra=3, max_num=3, widgets={'name': forms.TextInput(attrs={'class':'u-full-width'})})