
from django.contrib import admin

from .models import Project, Phase, Task, Participation


admin.site.register(Project)
admin.site.register(Phase)
admin.site.register(Task)
admin.site.register(Participation)
