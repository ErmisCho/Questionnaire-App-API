from django.db import models


class Survey(models.Model):
    """Represents a survey containing multiple questions."""
    name = models.CharField(max_length=100)
    key = models.UUIDField(primary_key=True)  # for easier test files....


class Question(models.Model):
    """Represents a question belonging to a survey."""
    name = models.CharField(max_length=100, default="Question 1")
    text = models.TextField()
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="questions"
    )


class AnswerOption(models.Model):
    """Represents an answer option for a specific question."""
    name = models.CharField(max_length=100, default="Option 1")
    key = models.UUIDField(primary_key=True)  # for easier test files....
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answeroptions"
    )


class Iteration(models.Model):
    """Represents an iteration (attempt) of answering a survey."""

    # Note: Keeping user as string is for simplification, since no user management system is implemented.
    user = models.CharField(max_length=100)
    key = models.UUIDField(primary_key=True)  # for easier test files....
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="iterations"
    )


class Answer(models.Model):
    """Represents an answer given in an iteration."""
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)
    additional_information = models.TextField(null=True)
    iteration = models.ForeignKey(
        Iteration, on_delete=models.CASCADE, related_name="given_answers"
    )
