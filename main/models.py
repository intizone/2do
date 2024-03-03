from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, null=True, blank=True)  # For category color coding

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('O', 'Ongoing'),
    )

    PRIORITY_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')  # New field for task priority
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)  # New field for when the task was completed

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # New field for when the comment was last updated

    def __str__(self):
        return self.comment_text[:50]

class Attachment(models.Model):  # New model for attachments on tasks
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name