from rest_framework import serializers
from .models import Survey, Question, AnswerOption, Iteration, Answer


class AnswerOptionSerializer(serializers.ModelSerializer):
    # Serializer for AnswerOption, handling JSON serialization for answer options.
    class Meta:
        model = AnswerOption
        fields = ['name', 'key', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    # Serializer for Question, including nested answer options.
    answeroptions = AnswerOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'name', 'text', 'answeroptions']


class SurveySerializer(serializers.ModelSerializer):
    # Serializer for Survey, including nested questions.
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ['name', 'key', 'questions']


class AnswerSerializer(serializers.ModelSerializer):
    # Serializer for Answer, handling user-provided responses.
    class Meta:
        model = Answer
        fields = ['answer_option', 'additional_information', 'iteration']


class IterationSerializer(serializers.ModelSerializer):
    # Serializer for Iteration, including nested answers and dynamic completion status.
    status = serializers.SerializerMethodField()
    given_answers = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Iteration
        fields = ['user', 'key', 'survey', 'status', 'given_answers']

    def get_status(self, obj):
        total_questions = obj.survey.questions.count()
        answered_questions = obj.given_answers.count()
        return 'completed' if answered_questions == total_questions else 'incomplete'
