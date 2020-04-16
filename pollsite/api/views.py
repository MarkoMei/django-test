# views.py
from rest_framework import viewsets

from .serializers import QuestionSerializer
from polls.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = QuestionSerializer