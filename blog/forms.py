from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=60,
                             widget=forms.TextInput(
                                 attrs = {"class": "form-control", "id": "comment-author-input", "placeholder": "Your name"}
                             ))
    body = forms.CharField(widget=forms.Textarea(
                                attrs = {"class": "form-control comment-body-input", "placeholder": "Leave a comment"}
                            ))