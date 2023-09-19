# myapp/models.py
from django.db import models

class ReportData(models.Model):
    # Определите поля вашей модели, соответствующие данным из вашей базы данных
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Добавьте другие поля по необходимости
    def __str__(self):
        return self.field1