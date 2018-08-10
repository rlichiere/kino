
from django.contrib import admin
from django.utils.html import format_html

from .models import Project, Phase, Task, TaskDependencies, Participation


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('label', 'referer_', )

    def referer_(self, instance):
        _referer = instance.referer
        return format_html('<a href="/admin/people/participant/%s/change/" target="_blank">%s</a>' % (_referer.id, _referer.name))


class PhaseAdmin(admin.ModelAdmin):
    list_display = ('label', 'rank', 'project', 'project_referer', )

    def project_referer(self, instance):
        _referer = instance.project.referer
        return format_html('<a href="/admin/people/participant/%s/change/" target="_blank">%s</a>' % (_referer.id, _referer.name))


class TaskAdmin(admin.ModelAdmin):
    list_display = ('label', 'project', 'phase', 'required_capacities_', 'referer_', 'depends_on_', )

    def project(self, instance):
        return instance.phase.project

    def required_capacities_(self, instance):
        if not instance.required_capacities:
            # todo : this should not happen because task.capacities should never be empty
            return '-'

        _urlsHtml = ''.join(
            [
                '<li><a href="/admin/people/capacity/%s/change/" target="_blank">%s</a></li>' % (_c.id, _c.label)
                for _c in instance.required_capacities.all()
            ])
        return format_html('<ul>%s</ul>' % _urlsHtml)

    def referer_(self, instance):
        _referer = instance.referer
        return format_html('<a href="/admin/people/participant/%s/change/" target="_blank">%s</a>' % (_referer.id, _referer.name))


    def depends_on_(self, instance):
        _taskDeps = TaskDependencies.objects.filter(concerned_task=instance)
        if _taskDeps.count() == 0:
            return '-'
        _urlsHtml = ''.join(
            [
                '<li><a href="/admin/project/taskdependency/%s/change/" target="_blank">%s</a></li>' % (_td.id, _td.depends_on)
                for _td in _taskDeps
            ])
        return format_html('<ul>%s</ul>' % _urlsHtml)


class TaskDependenciesAdmin(admin.ModelAdmin):
    list_display = ('project', 'phase', 'concerned_task', 'depends_on', )

    def project(self, instance):
        return instance.concerned_task.phase.project

    def phase(self, instance):
        return instance.concerned_task.phase


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('project', 'task', 'participant', 'validation')

    def project(self, instance):
        return instance.task.phase.project

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
admin.site.register(TaskDependencies, TaskDependenciesAdmin)
admin.site.register(Participation, ParticipationAdmin)
