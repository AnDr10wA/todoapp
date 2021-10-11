from django.urls import path, include
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
