from django import forms
from home.models import Note


class NoteForm(forms.Form):
    heading = forms.CharField(max_length=100)
    tags = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())


class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['heading', 'tags', 'content']
