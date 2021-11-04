from django import forms
from .models import Tweet

MAX_TWEET_LENGTH = 240


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_data(self):
        content = self.clean_data.get("content")
        if len(content)>MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content