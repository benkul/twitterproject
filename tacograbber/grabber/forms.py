from django import forms
from grabber.models import Bot, Current_Bot

class BotTokenForm(forms.ModelForm):

    class Meta:
        model = Current_Bot


class CreateTweet(forms.ModelForm):
    tweeted = forms.CharField(max_length=140, help_text="Compose Tweet Here")

    class Meta:
        model = Current_Bot
