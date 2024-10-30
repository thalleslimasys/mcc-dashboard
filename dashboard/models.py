from django.db import models
from django.db.models import JSONField
from numpy import true_divide


class Record(models.Model):
    state_details = JSONField(blank=True, null=True)
    state_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        managed = True
        db_table = "records"
