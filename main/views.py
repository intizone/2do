from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Comment, Category, Attachment
# from .froms import TaskForm, CommentForm, CategoryForm, AttachmentForm
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_edit.html', {'form': form})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_edit.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_edit.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_edit.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

@login_required
def comment_list(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = Comment.objects.filter(task=task)
    return render(request, 'comments/comment_list.html', {'task': task, 'comments': comments})

@login_required
def comment_new(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.task = task
            comment.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_edit.html', {'form': form})

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('task_detail', pk=comment.task.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/comment_edit.html', {'form': form})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        task_pk = comment.task.pk
        comment.delete()
        return redirect('task_detail', pk=task_pk)
    return render(request, 'comments/comment_confirm_delete.html', {'comment': comment})


@login_required
def attachment_new(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.task = task
            attachment.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = AttachmentForm()
    return render(request, 'attachments/attachment_edit.html', {'form': form})


@login_required
def attachment_delete(request, pk):
    attachment = get_object_or_404(Attachment, pk=pk)
    if request.method == "POST":
        task_pk = attachment.task.pk
        attachment.delete()
        return redirect('task_detail', pk=task_pk)
    return render(request, 'attachments/attachment_confirm_delete.html', {'attachment': attachment})