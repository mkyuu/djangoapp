from django import forms
from .models import Book,Comment


app_name = 'book_summary'

class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title','category','summary','publisher','img','link')


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title','comment')