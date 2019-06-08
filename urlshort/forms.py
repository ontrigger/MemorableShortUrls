from django import forms


class URLShortenForm(forms.Form):
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                'required': False,
                'placeholder': 'Enter your URL here',
                'class': 'form-control input-lg',
            }
        ),
        required=True,
    )
