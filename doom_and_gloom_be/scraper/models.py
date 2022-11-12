from django.db import models

class Todo(models.Model):
    company_name = models.CharField(max_length = 180)
    time_update = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    layoff_count = models.IntegerField()

    def __str__(self):
        return self.task