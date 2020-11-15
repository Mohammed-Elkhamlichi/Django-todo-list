# my Importing:
from django.shortcuts import (
    render,
    HttpResponseRedirect,
    get_object_or_404,
    redirect,
)
from django.http import HttpResponse
from .forms import (
    ToDoListForm,
    ToDoListUpdateForm
)
from .models import ToDoList
from django.template import loader
from datetime import datetime
# my Views:
thisYear = datetime.now().year

# To Do List Delete View:
def delete_to_do_list(request, id, title):
    ## QuerySet:
    task = get_object_or_404(ToDoList, id=id, title=title)
    ## Validations:
    if request.method == "POST":
        task.delete()
        return redirect('to_do_list')
    ## context:
    context = {
        "thisYear":thisYear,
        "task":task,
    }
    ## Template:
    template = loader.get_template('delete.html')
    return HttpResponse(template.render(context, request))


# To Do List Update View:
def update_to_do_list(request, id, title):
    ## QuerySet:
    obj = get_object_or_404(ToDoList, id=id, title=title)
    ## Form Validations:
    form = ToDoListUpdateForm(instance=obj)
    if request.method == "POST":
        form = ToDoListUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('to_do_list')
        else:
            return HttpResponseRedirect('.')
    ## Context:
    context = {
        "form":form,
        "thisYear":thisYear,
    }
    ## Template
    return render(request, 'update.html', context)


# To Do List View:
def to_do_list(request):
    ## QuerySet:
    lists = ToDoList.objects.all()
    ## form Validations:
    form = ToDoListForm()
    if request.method == "POST":
        form = ToDoListForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
        else:
            return HttpResponseRedirect(".")
    ## Context:
    context = {
        "form":form,
        "lists":lists,
        "thisYear":thisYear,
    }

    ## Template:
    return render(request, 'to_do_list.html', context)