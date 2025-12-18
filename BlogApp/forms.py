from django import forms
from . models import BlogTopic,BlogEntry

class BlogForm(forms.ModelForm):
  class Meta:
    model = BlogTopic
    fields = ['text']
    labels = {'text': ''}

class BlogEntriesForm(forms.ModelForm):
  class Meta:
    model = BlogEntry
    fields = ['postText']
    labels = {'postText': ''}
    widgets = {'postText': forms.Textarea(attrs={'cols': 80})}
    