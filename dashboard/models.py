from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(default='')

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

    def __str__(self):
        return self.title

class Homeworks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(default='')
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

