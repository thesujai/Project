# error_reporting/models.py

from django.db import models

class ErrorReport(models.Model):
    error_message = models.TextField()
    traceback = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Error Report"
        verbose_name_plural = "Error Reports"
        ordering = ['-timestamp']
    def __str__(self):
        return self.traceback
