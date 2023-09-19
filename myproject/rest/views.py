# report_app/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ReportData
from .serializers import ReportDataSerializer
from .report_generators import WordReportGenerator, ExcelReportGenerator
from django.http import FileResponse
import tempfile
import os

@api_view(['POST'])
def generate_report(request):
    format = request.data.get('format', 'word')  # Получите формат отчета из запроса (по умолчанию - Word)
    queryset = ReportData.objects.all()

    try:
        if format == 'word':
            generator = WordReportGenerator()
            document = generator.generate(queryset)
            temp_file_path = save_temp_document(document, "docx")
            return download_temp_file(temp_file_path, "report.docx")
        elif format == 'excel':
            generator = ExcelReportGenerator()
            workbook = generator.generate(queryset)
            temp_file_path = save_temp_document(workbook, "xlsx")
            return download_temp_file(temp_file_path, "report.xlsx")
    except Exception as e:
        return Response({"error": "An error occurred while generating the report."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def save_temp_document(document, file_extension):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}")
    temp_file_path = temp_file.name
    document.save(temp_file_path)
    return temp_file_path

def download_temp_file(temp_file_path, filename):
    response = FileResponse(open(temp_file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
