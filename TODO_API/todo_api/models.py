from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Todo(models.Model):
    class Meta(object):
        ordering = ['created_at']

    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    created_at = models.DateTimeField(default=now, blank=False)
    title = models.CharField(max_length=100, blank=True, default='')
    comments = models.CharField(max_length=200, blank=True, default='')
    status = models.CharField(max_length=10, default='Incomplete')
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title