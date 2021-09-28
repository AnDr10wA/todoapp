from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from .models import TodoModel
from .form import TodoFrom
from django.views import View
import smtplib
from datetime import datetime



def viewtasks(request):

    tasks = TodoModel.objects.all()

    return render(request, 'main.html', {'tasks':tasks})

class TodoFormView(View):
    form_class = TodoFrom
    initial = {'key':'value'}
    template_name = 'form.html'

    def get(self,request):

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            data = form.cleaned_data
            name = data['name']
            comment = data['comment']
            date_deadline = data['date_deadline']
            date_reminder = data['date_reminder']
            priority = data['priority']
            status = data['status']
            TodoModel.objects.create(name = name, comment = comment, date_deadline = date_deadline,
                                     date_reminder=date_reminder, priority=priority, status=status)

            return viewtasks(request)
        return render(request, self.template_name, {'form':form})


def task_detail_view(request, id):
    task = get_list_or_404(TodoModel, id=id)
    return render(request, 'detail.html', {'task':task[0]})



class TaskUpdateView(View):
    form_class = TodoFrom

    initial = {'key':'value'}
    template_name = 'form.html'
    def get(self, request, id):
        instance = TodoModel.objects.get(id=id)
        form = self.form_class(initial=self.initial, instance=instance)

        return render(request, self.template_name, {'form':form})
    def post(self,request, id):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            data = form.cleaned_data
            name = data['name']
            comment = data['comment']
            date_deadline = data['date_deadline']
            date_reminder = data['date_reminder']
            priority = data['priority']
            status = data['status']
            TodoModel.objects.filter(id=id).update(name = name, comment = comment, date_deadline = date_deadline,
                                     date_reminder=date_reminder, priority=priority, status=status)

            return viewtasks(request)
        return render(request, self.template_name, {'form':form})


def alertemail(request):
    fadd = 'applicationtodo243@gmail.com'
    tadd  = 'andr10wa@gmail.com'
    msg = 'hello, i am todoapplication'
    username = 'applicationtodo243@gmail.com'
    password = 'secret_todo'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(fadd, tadd, msg)

    return viewtasks(request)


def alertfunc(request):
    task = TodoModel.objects.filter(status = 'progress')
    for i in task:
        print(i.date_deadline)
        print(datetime.now())



    return viewtasks(request)

