# Create your views here.
from rest_framework import viewsets
from .models import Survey, Iteration, Question, AnswerOption, Answer
from .serializers import SurveySerializer, IterationSerializer, QuestionSerializer, AnswerOptionSerializer, AnswerSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    """Manages surveys (CRUD operations)."""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class IterationViewSet(viewsets.ModelViewSet):
    """Manages iterations (CRUD operations)."""
    queryset = Iteration.objects.all()
    serializer_class = IterationSerializer

    def perform_create(self, serializer):
        survey = serializer.validated_data['survey']
        if not Survey.objects.filter(key=survey.key).exists():
            raise ValidationError(
                f"Survey with key {survey.key} does not exist.")
        serializer.save()


class QuestionViewSet(viewsets.ModelViewSet):
    """Manages questions within a specific survey."""
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """Override the default queryset to filter questions by their parent survey."""
        if getattr(self, 'swagger_fake_view', False):
            return Question.objects.none()
        # Extract the survey ID from the URL
        survey_id = self.kwargs['survey_pk']
        # Retrieve questions for the specified survey
        return Question.objects.filter(survey_id=survey_id)

    def perform_create(self, serializer):
        # Set the survey for the new question
        survey_id = self.kwargs['survey_pk']
        serializer.save(survey_id=survey_id)


class AnswerOptionViewSet(viewsets.ModelViewSet):
    """Manages answer options within a specific question."""
    serializer_class = AnswerOptionSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Question.objects.none()
        # Get the parent question's ID from the URL
        question_id = self.kwargs['question_pk']
        return AnswerOption.objects.filter(question_id=question_id)

    def perform_create(self, serializer):
        # Set the question for the new answer option
        question_id = self.kwargs['question_pk']
        serializer.save(question_id=question_id)


class AnswerViewSet(viewsets.ModelViewSet):
    """Manages answers within a specific iteration."""
    serializer_class = AnswerSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Answer.objects.none()
        # Get the parent iteration's ID from the URL
        iteration_id = self.kwargs['iteration_pk']
        return Answer.objects.filter(iteration_id=iteration_id)

    def perform_create(self, serializer):
        # Set the iteration for the new answer
        iteration_id = self.kwargs['iteration_pk']
        serializer.save(iteration_id=iteration_id)
