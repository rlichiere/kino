
from django.db import models

from people.models import Capacity, Participant


class Project(models.Model):
    label = models.CharField(max_length=200)
    referer = models.ForeignKey(Participant)

    def __str__(self):
        return self.label


class Phase(models.Model):
    label = models.CharField(max_length=200)
    project = models.ForeignKey(Project)
    rank = models.PositiveIntegerField()

    def __str__(self):
        return self.label


class Task(models.Model):
    label = models.CharField(max_length=200)
    phase = models.ForeignKey(Phase)
    referer = models.ForeignKey(Participant)
    required_capacities = models.ManyToManyField(Capacity)

    def __str__(self):
        return self.label


class TaskDependencies(models.Model):
    concerned_task = models.ForeignKey(Task, related_name='depends')
    depends_on = models.ForeignKey(Task)


class Participation(models.Model):
    task = models.ForeignKey(Task)
    capacity = models.ForeignKey(Capacity)
    participant = models.ForeignKey(Participant)
    participant_validation = models.BooleanField(default=False)
    referer_validation = models.BooleanField(default=False)

    def __str__(self):
        if self.participant_validation and self.referer_validation:
            _verb = 'participates'
        elif self.participant_validation and not self.referer_validation:
            _verb = 'wants to participate'
        elif not self.participant_validation and self.referer_validation:
            _verb = 'is invited to participate'
        else:
            _verb = 'stopped to participate'
        return '%s %s on %s as %s' % (self.participant, _verb, self.task, self.capacity)
