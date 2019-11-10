from django.db import models
from django_random_queryset import RandomManager


class QCollection(models.Model):
    name = models.CharField(max_length=50)
    amount_of_questions_per_session = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=200)
    related_qcollection = models.ForeignKey(QCollection,
                                            on_delete=models.CASCADE
                                            )
    objects = RandomManager()

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('mainland:q_detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
