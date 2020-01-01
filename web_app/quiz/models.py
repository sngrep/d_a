from django.db import models
from mainland.models import Question
from django.contrib.auth.models import User


class Attempt(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    time_of_attempt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Choices(models.Model):
    related_attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer_true = models.BooleanField()
