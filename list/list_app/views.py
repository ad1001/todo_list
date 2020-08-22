from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .models import List
from .forms import TodoForm

# Create your views here.
def index(request):
    arr = List.objects.order_by("-date")[::-1]
    form = TodoForm()
    context = {"List": arr,"form":form}
    return render(request,"list_app/index.html",context = context)


def addItem(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            return HttpResponseRedirect("/")

def complete(request, todo_id):
    todo = List.objects.get(pk = todo_id)
    todo.completed = True
    todo.save()

    return HttpResponseRedirect("/")

def remove(request):
    todo = List.objects.filter(completed = True).delete()
    return HttpResponseRedirect("/")


    
    
    
