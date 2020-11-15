# my Importing:
from django.db import models

# my Models:

## To Do List Model:
class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    completed  = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-updated']
