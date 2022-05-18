from django.contrib import admin
from todo.models import Task, Tag, Note

# Register your models here.
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Note)