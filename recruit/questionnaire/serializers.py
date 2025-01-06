from rest_framework import serializers

from questionnaire.models import Survey, Question, AnswerOption, Iteration, Answer


class AnswerOptionSerializer(serializers.ModelSerializer):
    """Serializer for AnswerOption, handling JSON serialization for answer options."""
    class Meta:
        model = AnswerOption
        fields = ['name', 'key', 'question']

    def validate_question(self, value):
        """Validate that the referenced question exists in the database."""
        if not Question.objects.filter(id=value.id).exists():
            raise serializers.ValidationError(
                "The referenced question does not exist.")
        return value


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for Question, including nested answer options."""
    answeroptions = AnswerOptionSerializer(
        many=True, read_only=True)  # Include related answer options

    class Meta:
        model = Question
        fields = ['id', 'name', 'text', 'answeroptions']

    def validate_survey(self, value):
        """Validate that the survey associated with the question exists."""
        if not Survey.objects.filter(key=value.key).exists():
            raise serializers.ValidationError(
                "The survey with the provided key does not exist.")
        raise value


class SurveySerializer(serializers.ModelSerializer):
    """Serializer for Survey, including nested questions."""
    questions = QuestionSerializer(
        many=True, read_only=True)  # Include related questions

    class Meta:
        model = Survey
        fields = ['name', 'key', 'questions']


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for Answer, which handles user-provided responses to questions.
    Includes nested details for the associated answer option.
    """
    answer_option_details = AnswerOptionSerializer(
        source='answer_option', read_only=True)  # Include detailed information about the answer option

    class Meta:
        model = Answer
        fields = ['answer_option', 'answer_option_details',
                  'additional_information', 'iteration']

    def validate_answer_option(self, value):
        """Validate that the referenced answer option exists in the database."""
        if not AnswerOption.objects.filter(key=value.key).exists():
            raise serializers.ValidationError(
                "The referenced answer option does not exist.")
        return value

    def validate_iteration(self, value):
        """Validate that the referenced iteration exists in the database."""
        if not Iteration.objects.filter(key=value.key).exists():
            raise serializers.ValidationError(
                "The referenced iteration does not exist.")
        return value


class IterationSerializer(serializers.ModelSerializer):
    """
    Serializer for Iteration, which tracks a user's progress through a survey.
    Includes nested answers and dynamically calculates the completion status.
    """
    status = serializers.SerializerMethodField()
    given_answers = AnswerSerializer(
        many=True, read_only=True)

    class Meta:
        model = Iteration
        fields = ['user', 'key', 'survey', 'status', 'given_answers']

    def validate_survey(self, value):
        """Validate that the survey exists in the database."""
        if not Survey.objects.filter(key=value.key).exists():
            raise serializers.ValidationError(
                "The survey with the provided key does not exist.")
        return value

    def get_status(self, obj):
        """Calculate the completion status of the iteration."""
        total_questions = obj.survey.questions.count()
        answered_questions = obj.given_answers.count()
        return 'completed' if answered_questions == total_questions else 'incomplete'
