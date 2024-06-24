from django import forms
from c_app.models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model= ContactMessage
        fields = '__all__'