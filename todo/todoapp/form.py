from django.forms import ModelForm
from .models import TodoModel


class TodoFrom(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update( placeholder="ваш to do")
        self.fields['name'].widget.attrs.update({"class": "form-control"})
        self.fields['name'].widget.attrs.update({"onfocus": "clearThis(this)"})

    class Meta:
        model = TodoModel
        fields = ("name",)
