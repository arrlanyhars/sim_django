from django.db import models

from datetime import timezone

class Classroom(models.Model):
    cl_id = models.AutoField(primary_key=True)
    cl_name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'class'