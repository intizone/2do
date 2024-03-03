from django.urls import path
from .views import (category_list, category_new, category_edit, category_delete,
                    task_list, task_detail, task_new, task_edit, task_delete,
                    comment_new, comment_edit, comment_delete, attachment_new, attachment_delete,
                    attachment_new, attachment_delete,
                    )

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('category/new/', category_new, name='category_new'),
    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),

    path('task/', task_list, name='task_list'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/new/', task_new, name='task_new'),
    path('task/<int:pk>/edit/', task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),

    path('task/<int:pk>/comment/new/', comment_new, name='comment_new'),
    path('comment/<int:pk>/edit/', comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', comment_delete, name='comment_delete'),

    path('task/<int:pk>/attachment/new/', attachment_new, name='attachment_new'),
    path('attachment/<int:pk>/delete/', attachment_delete, name='attachment_delete'),
]
