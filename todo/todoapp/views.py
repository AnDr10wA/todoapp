import os

from django.shortcuts import render, redirect
from django.views.generic import View
from .models import TodoModel
from .form import TodoFrom


class MainView(View):
    form = TodoFrom

    def post(self,request):
        if request.method == 'POST' and 'btn-add' in request.POST:
            self.form = TodoFrom(request.POST)
            if self.form.is_valid():
                self.form.save()


        elif request.method == 'POST' and 'btn-del' in request.POST:
            task = TodoModel.objects.filter(pk=request.POST['btn-del'])
            task.delete()

        elif request.method == 'POST' and 'btn-edit' in request.POST:
            self.form = TodoFrom(request.POST)
            if self.form.is_valid():
                task = TodoModel.objects.filter(pk=request.POST['btn-edit'])
                for i in task:
                    print(request.POST)
                    i.name = request.POST['name']
                    i.save()

        elif request.method == 'POST' and 'btn-slide' in request.POST:
            task = TodoModel.objects.filter(pk=request.POST['btn-slide'])
            for i in task:
                i.status = True
                i.save()

        elif request.method == 'POST' and 'btn-slide-back' in request.POST:
            task = TodoModel.objects.filter(pk=request.POST['btn-slide-back'])
            for i in task:
                i.status = False
                i.save()

        return self.get(request)


    def get(self, request):
        tasks_in = TodoModel.objects.filter(status=False)
        tasks_done = TodoModel.objects.filter(status=True)
        return render(request, 'main.html', {'form': self.form, 'tasks_in': tasks_in,
                                             'tasks_done': tasks_done})

