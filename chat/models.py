from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class UserModel(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="chat_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="chat_user_permissions", blank=True)

    def __str__(self):
        return self.username

class PromptTemplate(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name