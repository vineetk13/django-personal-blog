from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=60,
                             widget=forms.TextInput(
                                 attrs = {"class": "form-control", "placeholder": "Your name", "style": "width: 200px;"}
                             ))
    body = forms.CharField(widget=forms.Textarea(
                                attrs = {"class": "form-control", "placeholder": "Leave a comment", "style": "width: 500px; height: 150px; resize: none"}
                            ))