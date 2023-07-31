from django.shortcuts import render, redirect
from Database.forms import Workerform
from Database.models import Worker

# Create your views here.

def index(request):
    if request.method == "POST":
        form = Workerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = Workerform()
    return render(request,'index.html',{'form':form})

def show(request):
    workers=Worker.objects.all()
    return render(request,'show.html',{'workers':workers})

def edit(request,id):
    worker=Worker.objects.get(id=id)
    return render(request,'edit.html',{'worker':worker})

def delete(request,id):
    worker=Worker.objects.get(id=id)
    worker.delete()
    return redirect('show')

def update(request, id):
    worker = Worker.objects.get(id=id)
    if request.method == "POST":
        form = Workerform(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = Workerform(instance=worker)  # Pass the instance to pre-fill the form
    return render(request, 'show.html', {'form': form, 'worker': worker})


