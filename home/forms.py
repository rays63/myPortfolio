from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email','class':'form-control'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject','class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message','class':'form-control'}))