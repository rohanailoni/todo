from django.shortcuts import render
from app.models import todo
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
import datetime
# Create your views here.
def index(request):
    t=todo.objects.all()
    return render(request,'index.html',{"t":t})




def addtodo(request):
    while True:
        id=randint(1,10000)
        if todo.objects.filter(todo_id=id).exists()==False:
            break;
    print(request.method)
    r=request.POST.get('t')
    print(r)
    date_cre=datetime.datetime.now()
    
    
    todo(todo_item=r,date_item=date_cre,todo_id=id).save()
    print("after adding into the database")
    return HttpResponseRedirect('/index/')




def deletetodo(request,todo_id):
    todo.objects.get(todo_id=todo_id).delete()
    return HttpResponseRedirect('/index/')
    