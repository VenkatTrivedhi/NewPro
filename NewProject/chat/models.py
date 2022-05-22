from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    message  = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_by')

