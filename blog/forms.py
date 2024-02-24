from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
                                attrs = {"class": "form-control", "placeholder": "Leave a comment", "style": "width: 500px; height: 150px; resize: none"}
                            ))