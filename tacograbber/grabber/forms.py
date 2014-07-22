from django import forms
from grabber.models import Bot, Current_Bot

class BotForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the Bot name.")

    class Meta:
        model = Bot


class CreateTweet(forms.ModelForm):
    tweeted = forms.CharField(max_length=140, help_text="Compose Tweet Here")

    class Meta:
        model = Current_Bot
