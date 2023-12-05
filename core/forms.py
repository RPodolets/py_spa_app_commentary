from django import forms


class CommentaryForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    home_url = forms.URLField(label="Home url", required=False)
    text = forms.CharField(widget=forms.Textarea)
