from django import forms
from rango.models import Bot

class BotForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the Bot name.")

    class Meta:
        model = Bot
