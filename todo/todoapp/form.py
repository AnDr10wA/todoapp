from django.forms import ModelForm
from .models import TodoModel

class TodoFrom(ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
