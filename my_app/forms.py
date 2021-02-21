from django import forms
from .models import new_note

class NoteForm(forms.ModelForm):
  class Meta:
    model = new_note
    fields = ['alias', 'note',]