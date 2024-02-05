from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView



class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 't1'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'kat'
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'delta'
    fields=('name','priority','date')
    def get_success_url(self, ):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



def demo(request):
    t2=Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        t=Task(name=name,priority=priority,date=date)
        t.save()
    return render(request,'home.html',{'t1':t2})

 # def details(request):
 #    t=Task.objects.all()
 #    return render(request,'details.html',{'t':t})

def delete(request,taskid):
    tk=Task.objects.get(id=taskid)
    if request.method=='POST':
        tk.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    tsk=Task.objects.get(id=id)
    form=Todoform(request.POST or None,instance=tsk)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'f':form,'task':tsk})
