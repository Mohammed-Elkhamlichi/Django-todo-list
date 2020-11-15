# my Importing:
from django import forms
from .models import ToDoList

# my Forms:

## To Do List Form:
class ToDoListForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class":"col-md-10 p-3 border rounded",
                "placeholder":"To Do List Title"
            }
        )
    )
    # completed = forms.CharField(
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             "class":"p-3 border rounded text-light"
    #         }
    #     )
    # )
    class Meta:
        model = ToDoList
        fields = ('__all__')

class ToDoListUpdateForm(ToDoListForm):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class":"col-md-12 p-3 border rounded",
                "placeholder":"To Do List Title"
            }
        )
    )