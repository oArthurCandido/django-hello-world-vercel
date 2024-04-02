from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.
def home(request):
    return render (request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def salvar(request):
    title = request.POST.get("title")
    completed =  True if request.POST.get("completed") else False
    print('isCompleted', completed)
    TodoItem.objects.create(title=title, completed=completed)
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def series(request):
    return render(request,"6aserieA.html" )