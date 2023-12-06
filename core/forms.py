from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Reset
from django import forms


class CommentaryForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    home_url = forms.URLField(label="Home url", required=False)
    text = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-5'
        self.helper.layout = Layout(
            Row(
                'username', "email", 'home_url',
                css_class='form-row'
            ),
            'text',
            Row(
                'captcha',
                Submit('submit', 'Comment', css_class='btn btn-primary', style='width: 100px;'),
                Reset('reset', 'Reset', css_class='btn btn-secondary', style='width: 100px;'),
            )
        )
