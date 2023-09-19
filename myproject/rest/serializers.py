# report_app/serializers.py
from rest_framework import serializers
from .models import ReportData

class ReportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportData
        fields = '__all__'
