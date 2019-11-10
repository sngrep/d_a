from django.db import models
from mainland.models import Question, Answer
from django.contrib.auth.models import User


class Choices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices_selected = models.ForeignKey(Answer, on_delete=models.CASCADE)
    time_of_attempt = models.DateTimeField(auto_now_add=True)
