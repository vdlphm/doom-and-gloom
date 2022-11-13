from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length = 180)
    time_update = models.DateTimeField()
    layoff_count = models.IntegerField()

    def __str__(self):
        return self.task