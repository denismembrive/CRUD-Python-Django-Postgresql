from urllib import request
from django.shortcuts import render, redirect
from .models import Task  # Importamos la clase Task desde models

# Create your views here.
# Creamos la funcion que va a leer el archivo html y darle intereaccion

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": tasks})


def create_task(request):
    new_title = request.POST["title"]
    new_description = request.POST["description"]
    if new_title == "" or new_description == "":
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html", {"tasks": tasks, "error": "Title and description is required"}
        )
    task = Task(title=new_title, description=new_description)
    task.save()
    return redirect("/tasks/")


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/tasks/")
