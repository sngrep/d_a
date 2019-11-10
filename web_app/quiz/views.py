from django.shortcuts import render, get_object_or_404
from mainland.models import Question
from django.views import generic
from django.contrib import messages


class QuizStartView(generic.ListView):
    template_name = 'quiz/quizstart_list.html'
    context_object_name = 'question_list'

    def get_queryset(self, **kwargs):
        queryset = Question.objects.filter(related_qcollection=1)
        # return Question.objects.get()
        # return Question.objects.order_by('?').first()
        return queryset.random()


class QuizResultsDetail(generic.DetailView):
    model = Question
    template_name = 'quiz/quizresults_detail.html'


def get_selected_choices(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choices = request.POST.getlist('choices')
    try:
        corrects = []
        for answer_check in question.answer_set.all():
            if answer_check.correct is True:
                corrects.append(str(answer_check.id))
        print(corrects)
        if corrects == selected_choices:
            messages.success(request, 'correct!')
        else:
            messages.error(request, 'not correct!')
    except (KeyError):
        return render(
                    request,
                    'quiz/quizresults_detail.html',
                    context={'choices': selected_choices}
                    )
    else:
        print(f'{selected_choices}')
        return render(
                    request,
                    'quiz/quizresults_detail.html',
                    {'choices': selected_choices}
                    )
