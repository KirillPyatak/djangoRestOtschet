from django.db import models

class ReportData(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    # Добавьте другие поля, если они нужны

    def __str__(self):
        return self.field1
