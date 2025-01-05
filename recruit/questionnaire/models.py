from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=100)
    key = models.UUIDField(primary_key=True)  # for easier test files....


class Question(models.Model):
    name = models.CharField(max_length=100, default="Question 1")
    text = models.TextField()
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="questions"
    )


class AnswerOption(models.Model):
    name = models.CharField(max_length=100, default="Option 1")
    key = models.UUIDField(primary_key=True)  # for easier test files....
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answeroptions"
    )


class Iteration(models.Model):
    # user as string is for simplification, since no user management system is implemented.
    user = models.CharField(max_length=100)
    key = models.UUIDField(primary_key=True)  # for easier test files....
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="iterations"
    )


class Answer(models.Model):
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)
    additional_information = models.TextField(null=True)
    iteration = models.ForeignKey(
        Iteration, on_delete=models.CASCADE, related_name="given_answers"
    )
