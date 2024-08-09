from django.db import models

from datetime import timezone

class City(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'city'