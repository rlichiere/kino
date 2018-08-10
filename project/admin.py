
from django.contrib import admin

from .models import Project, Phase, Task, TaskDependency, Participation


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('label', 'referer_', )

    def referer_(self, instance):
        return instance.referer.representation.as_link()


class PhaseAdmin(admin.ModelAdmin):
    list_display = ('label', 'rank', 'project', 'project_referer', )

    def project_referer(self, instance):
        return instance.project.referer.representation.as_link()


class TaskAdmin(admin.ModelAdmin):
    list_display = ('label', 'project', 'phase_', 'required_capacities_', 'referer_', 'depends_on_', )

    def project(self, instance):
        return instance.phase.project.representation.as_link()

    def phase_(self, instance):
        return instance.phase.representation.as_link()

    def required_capacities_(self, instance):
        if not instance.required_capacities:
            # todo : this should not happen because task.capacities should never be empty
            return '-'

        return instance.representation.as_list(instance.required_capacities.all())

    def referer_(self, instance):
        return instance.referer.representation.as_link()

    def depends_on_(self, instance):
        _taskDeps = TaskDependency.objects.filter(concerned_task=instance)
        return instance.referer.representation.as_list(_taskDeps)


class TaskDependencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'concerned_task', 'depends_on', 'phase', 'project', )

    def phase(self, instance):
        return instance.concerned_task.phase.representation.as_link()

    def project(self, instance):
        return instance.concerned_task.phase.project.representation.as_link()


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant_', 'capacity_', 'task_', 'validation', 'project')

    def task_(self, instance):
        return instance.task.representation.as_link()

    def participant_(self, instance):
        return instance.participant.representation.as_link()

    def capacity_(self, instance):
        return instance.capacity.representation.as_link()

    def project(self, instance):
        return instance.task.phase.project.representation.as_link()

    def validation(self, instance):
        if instance.participant_validation and instance.referer_validation:
            _verb = 'ok'
        elif instance.participant_validation and not instance.referer_validation:
            _verb = 'proposed'
        elif not instance.participant_validation and instance.referer_validation:
            _verb = 'invited'
        else:
            _verb = 'cancelled'
        return _verb


admin.site.register(Project, ProjectAdmin)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskDependency, TaskDependencyAdmin)
admin.site.register(Participation, ParticipationAdmin)
