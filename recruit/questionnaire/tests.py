# Create your tests here or in a dedicated tests/ directory.
from questionnaire.models import Survey, Iteration, Question, AnswerOption, Answer
from rest_framework.test import APITestCase
from rest_framework import status
from questionnaire.models import Survey


class SurveyAPITest(APITestCase):
    def test_create_survey(self):
        """Test if a survey can be created successfully."""
        response = self.client.post('/surveys/', {
            "name": "Customer Feedback Survey",
            "key": "123e4567-e89b-12d3-a456-426614174000"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(Survey.objects.first().name,
                         "Customer Feedback Survey")


class IterationAPITest(APITestCase):
    def setUp(self):
        """Set up test data."""
        self.survey = Survey.objects.create(
            name="Test Survey", key="123e4567-e89b-12d3-a456-426614174001")
        self.question = Question.objects.create(
            name="Question 1", text="How do you rate our service?", survey=self.survey)
        self.answer_option = AnswerOption.objects.create(
            name="5 stars", key="423e4567-e89b-12d3-a456-426614174002", question=self.question)

    def test_create_iteration(self):
        """Test if an iteration can be created successfully."""
        response = self.client.post('/iterations/', {
            "user": "test_user",
            "key": "423e4567-e89b-12d3-a456-426614174003",
            "survey": str(self.survey.key)
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Iteration.objects.count(), 1)

    def test_iteration_status(self):
        """Test if iteration status updates correctly."""
        iteration = Iteration.objects.create(
            user="test_user", key="423e4567-e89b-12d3-a456-426614174004", survey=self.survey)
        Answer.objects.create(iteration=iteration,
                              answer_option=self.answer_option)
        response = self.client.get(f'/iterations/{iteration.key}/')
        self.assertEqual(response.data['status'], 'completed')


class QuestionAPITest(APITestCase):
    def setUp(self):
        """Set up test data."""
        self.survey = Survey.objects.create(
            name="Test Survey", key="123e4567-e89b-12d3-a456-426614174005")

    def test_add_question_to_survey(self):
        """Test if a question can be added to a survey."""
        response = self.client.post(f'/surveys/{self.survey.key}/questions/', {
            "name": "Question 1",
            "text": "What is your favorite color?"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.survey.questions.count(), 1)
        self.assertEqual(self.survey.questions.first().text,
                         "What is your favorite color?")
