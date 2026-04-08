from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=100)


class task(models.Model):
    id = models.AutoField(primary_key=True)
    tareas = models.CharField(max_length=255, db_column='Tareas')

    class Meta:
        db_table = 'dashboard_tasks'
        managed = False