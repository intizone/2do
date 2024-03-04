from django.urls import path
from .views import (category_list, category_edit,
                    task_list, task_detail, task_edit,
                    )

urlpatterns = [
    # category
    path('category/', category_list, name='category_list'),
    path('category/edit/<int:pk>', category_edit, name='category_edit'),
    # task
    path('task/', task_list, name='task_list'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/edit/<int:pk>', task_edit, name='task_edit'),
]
