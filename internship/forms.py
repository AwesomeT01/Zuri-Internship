from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type' :"text",'class':"form-control", 'placeholder':"David Mark"}))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type' :"email",'class':"form-control", 'placeholder':"davidmark@email.com"}))
    message = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'type' :"text",'class':"form-control", 'rows': "5"}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']