from django.db import models

class Comment(models.Model):
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
