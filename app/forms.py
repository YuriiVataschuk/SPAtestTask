import os

from django.core.exceptions import ValidationError
from django.forms import ImageField, FileField
import bleach
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    def validate_text_file(value):
        max_size = 100 * 1024  # 100KB
        allowed_formats = ['.txt']

        if value:
            if value.size > max_size:
                raise ValidationError("File size exceeds the maximum limit of 100KB.")

            ext = os.path.splitext(value.name)[1].lower()
            if ext not in allowed_formats:
                raise ValidationError("Invalid file format. Allowed format: TXT")

    image = ImageField(required=False)
    text_file = FileField(required=False, validators=[validate_text_file])

    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'text', 'image', 'text_file']

    def clean_text(self):
        text = self.cleaned_data['text']
        return bleach.clean(text, tags=bleach.sanitizer.ALLOWED_TAGS, strip=True)
