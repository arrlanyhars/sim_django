from django.db import models

from datetime import timezone
# Create your models here.

class Users(models.Model):
    u_id = models.BigAutoField(primary_key=True)
    u_fullname = models.CharField(max_length=200, null=True)
    u_nickname = models.CharField(max_length=200, null=True)
    u_email = models.CharField(max_length=200, null=True, unique=True)
    u_password = models.CharField(max_length=200, null=False)
    u_whatsapp_number = models.CharField(max_length=200, null=True)
    # u_created_at = models.DateTimeField(default=timezone.now)
    # u_updated_at = models.DateTimeField(default=timezone.now)
    # u_deleted_at = models.DateTimeField(default=timezone.now)
    u_created_at = models.DateTimeField(default=None)
    u_updated_at = models.DateTimeField(default=None)
    u_deleted_at = models.DateTimeField(default=None)
    u_created_by = models.CharField(max_length=200, null=True)
    u_updated_by = models.CharField(max_length=200, null=True)
    u_deleted_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'users'