import bleach
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'text']

    def clean_text(self):
        text = self.cleaned_data['text']
        return bleach.clean(text, strip=True, tags=bleach.sanitizer.ALLOWED_TAGS)
