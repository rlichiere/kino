
from django.db import models


class Project(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label
