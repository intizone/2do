from django.contrib import admin
from .models import Task, Comment, Category, Attachment

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Attachment)
