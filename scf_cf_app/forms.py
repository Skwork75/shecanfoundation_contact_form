from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta :
        model = Contact
        fields = ['name', 'email', 'message']
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name should not contain numbers.")
        return name
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message should be at least 10 characters long.")
        elif len(message) > 500:
            raise forms.ValidationError("Message should not exceed 500 characters.")
        return message