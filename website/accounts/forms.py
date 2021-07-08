from django import forms
 

 
class PasswordResetForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    