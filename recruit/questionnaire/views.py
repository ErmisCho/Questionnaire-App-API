# Create your views here.
from rest_framework import viewsets
from .models import Survey, Iteration, Question, AnswerOption, Answer
from .serializers import SurveySerializer, IterationSerializer, QuestionSerializer, AnswerOptionSerializer, AnswerSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    # Manages surveys (CRUD operations).
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class IterationViewSet(viewsets.ModelViewSet):
    # Manages iterations (CRUD operations).
    queryset = Iteration.objects.all()
    serializer_class = IterationSerializer
