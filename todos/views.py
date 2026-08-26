from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    total = todos.count()
    completed = todos.filter(completed=True).count()
    pending = total - completed
    return render(request, "todos/index.html", {
        "todos": todos,
        "total": total,
        "completed": completed,
        "pending": pending,
    })

def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        if title:
            Todo.objects.create(title=title, description=description)
    return redirect("todo_list")

def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save(update_fields=["completed"])
    return redirect("todo_list")

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("todo_list")
