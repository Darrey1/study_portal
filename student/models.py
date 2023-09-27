from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# Notes
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(default=datetime.now)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
# Todo
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    due_date = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'
#homework
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Homework'
        verbose_name_plural = 'Homework'
        
        
    

