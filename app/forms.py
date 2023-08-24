from captcha.fields import ReCaptchaField
from django.forms import ImageField, FileField
import bleach
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    image = ImageField(required=False)
    text_file = FileField(required=False)
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'text', 'image', 'text_file', 'captcha']

    def clean_text(self):
        text = self.cleaned_data['text']
        return bleach.clean(text, strip=True, tags=bleach.sanitizer.ALLOWED_TAGS)
