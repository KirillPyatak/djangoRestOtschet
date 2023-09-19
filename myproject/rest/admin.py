from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ReportData)
class data(ReportData):
    field1 = 'Первая запись'
    field2 = 'Вторая запись'