from django.shortcuts import render, get_object_or_404
from mainland.models import Question, QCollection
from django.views import generic
from .forms import ChoicesForm, AttemptForm
from quiz.models import Attempt
import string
import random


class ChooseCollectionView(generic.ListView):
    model = QCollection
    template_name = 'quiz/choosecollection_list.html'
    paginate_by = 10


class QuizStartView(generic.ListView):
    template_name = 'quiz/quizstart_list.html'
    context_object_name = 'question_list'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        qc_pk = self.kwargs.get('pk')
        queryset = Question.objects.filter(related_qcollection=qc_pk)
        print(QCollection.objects.get(pk=qc_pk).amount_of_questions_per_session)
        return queryset.random(QCollection.objects.get(pk=qc_pk).amount_of_questions_per_session)


class QuizResultsDetail(generic.DetailView):
    model = Question
    template_name = 'quiz/quizresults_detail.html'


def get_raw_answers(request, **kwargs):
    raw_dict = {}
    for objkey in request.POST:
        if 'question_pk|' in objkey:
            tmp = objkey.strip('question_pk|')
            raw_dict[int(tmp)] = request.POST.getlist(objkey)
    context_corrects = get_selected_choices(request, raw_dict)
    return render(
                request,
                'quiz/quizresults_detail.html',
                context={'choices': None, 'context_corrects': context_corrects}
                )


def get_selected_choices(request, raw_dict):
    attempt_set = AttemptForm()
    attempt_set = attempt_set.save(commit=False)
    attempt_set.username = request.user
    l_a_d = string.ascii_letters + string.digits
    attempt_set.name = f"{request.user}_{''.join(random.choice(l_a_d) for i in range(10))}"
    attemp_name = attempt_set.name
    attempt_set.save()
    corrects_count = 0

    for quest in raw_dict:
        question = get_object_or_404(Question, pk=quest)

        corrects = []
        incorrects = []
        for answer_check in question.answer_set.all():
            if answer_check.correct is True:
                corrects.append(str(answer_check.id))

        choice_form = ChoicesForm()
        choice_form = choice_form.save(commit=False)
        choice_form.related_attempt = Attempt.objects.get(name=attemp_name)
        choice_form.question = question
        if corrects == raw_dict[quest]:
            choice_form.answer_true = True
            corrects_count += 1
        else:
            choice_form.answer_true = False
            incorrects.append(question)
        try:
            choice_form.save()
        except ValueError:
            print(choice_form)

    return [corrects_count, question.related_qcollection.amount_of_questions_per_session, incorrects]
