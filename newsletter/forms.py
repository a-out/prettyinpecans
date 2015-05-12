from django import forms

class SubscribeForm(forms.Form):
    email = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'id': 'subscribe-input',
                'class': 'sidebar-form-input',
                'placeholder': 'Email'
            }
        )
    )