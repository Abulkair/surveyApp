from .models import Survey
from rest_framework import viewsets, permissions
from .serializers import SurveySerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = SurveySerializer