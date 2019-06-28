from django import forms
from .models import Book,Comment,TopCategory,BigCategory,Category,Publisher,Author


app_name = 'book_summary'

class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title','summary','author','publisher','category','img','link','user')


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title','comment')