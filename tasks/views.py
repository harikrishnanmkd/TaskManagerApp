from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def dashboard(request):

    filter_type = request.GET.get("filter", "all")

    tasks = Task.objects.filter(user=request.user)

    if filter_type == "completed":
        tasks = tasks.filter(completed=True)

    elif filter_type == "pending":
        tasks = tasks.filter(completed=False)

    return render(request, "dashboard.html", {
        "tasks": tasks,
        "filter": filter_type
    })


@login_required
def add_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect("dashboard")

    else:
        form = TaskForm()

    return render(request, "task_form.html", {"form": form})


@login_required
def edit_task(request, pk):

    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = TaskForm(instance=task)

    return render(request, "task_form.html", {"form": form})


@login_required
def delete_task(request, pk):

    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("dashboard")

    return render(request, "task_confirm_delete.html", {"task": task})


@login_required
def complete_task(request, pk):

    task = get_object_or_404(Task, pk=pk, user=request.user)

    task.completed = True
    task.save()

    return redirect("dashboard")