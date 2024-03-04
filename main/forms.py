from django import forms
from .models import Task, Category, Comment, Attachment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title',
                  'description', 
                  'status', 
                  'priority', 
                  'category', 
                  'due_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']