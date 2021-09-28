from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('', viewtasks),
    path('createtask', TodoFormView.as_view(), name='createtask'),
    path('<int:id>', task_detail_view, name='detailtask'),
    path('update/<int:id>', TaskUpdateView.as_view(), name='updatetask'),
    path('sendmail', alertemail),
    path('alert', alertfunc),

]
