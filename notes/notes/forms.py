from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note #links the form to the note model
        fields = ['title', 'content']
