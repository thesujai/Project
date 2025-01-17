# error_reporting/models.py

from django.db import models

class ErrorReport(models.Model):
    errorFrom = models.CharField(max_length=100, default="Backend")
    error_message = models.TextField()
    traceback = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Error Report"
        verbose_name_plural = "Error Reports"
        ordering = ['-timestamp']
    def __str__(self):
        return self.traceback
