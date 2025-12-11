from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todo_list(request):
    # Додати нову задачу
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Todo.objects.create(title=title)
        return redirect("todo_list")

    todos = Todo.objects.order_by("-created_at")
    return render(request, "core/todo_list.html", {"todos": todos})


def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect("todo_list")


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("todo_list")
# Create your views here.
def landing(request):
    return render(request, 'core/landing.html')
