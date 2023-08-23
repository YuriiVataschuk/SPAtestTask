import bleach
from django.db import models


class Comment(models.Model):
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def clean_text(self):
        return bleach.clean(self.text, strip=True, tags=bleach.sanitizer.ALLOWED_TAGS)
