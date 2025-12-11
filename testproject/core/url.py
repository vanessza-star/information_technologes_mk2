from django.urls import path
from .views import todo_list, toggle_todo, delete_todo

urlpatterns = [
    path("todo/", todo_list, name="todo_list"),
    path("todo/<int:pk>/toggle/", toggle_todo, name="toggle_todo"),
    path("todo/<int:pk>/delete/", delete_todo, name="delete_todo"),
]
