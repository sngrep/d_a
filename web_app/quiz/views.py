from django.shortcuts import render, get_object_or_404
from mainland.models import Question, QCollection, Answer
from django.core.cache import cache
from django.views import generic
import secrets


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
        quests_list = dict()
        queryset = Question.objects.filter(related_qcollection=qc_pk)
        quests_list['count'] = QCollection.objects.get(pk=qc_pk).amount_of_questions_per_session
        queryset_data = queryset.random(quests_list['count'])
        uid = secrets.token_hex(16)
        self.request.session['question_session_id'] = uid

        tmp_list = list()
        for question in queryset_data:
            tmp_list.append(question.id)
        quests_list['questions'] = tmp_list
        cache.set(uid, quests_list)
        return queryset_data


class QuizResultsDetail(generic.DetailView):
    model = Question
    template_name = 'quiz/quizresults_detail.html'


def get_raw_answers(request):
    raw_dict = {}
    for objkey in request.POST:
        if 'question_pk=' in objkey:
            tmp = objkey.strip('question_pk=')
            temp_val_list = list()
            for value in request.POST.getlist(objkey):
                temp_val_list.append(int(value))
            raw_dict[int(tmp)] = temp_val_list
    quests_from_get = get_quests_cached(request)
    context_corrects = compare_answers(quests_from_get['questions'], raw_dict)
    return render(
                request,
                'quiz/quizresults_detail.html',
                context={'choices': None,
                         'context_corrects': context_corrects,
                         'corrects_count': context_corrects['corrects_count'],
                         'incorrects_list': context_corrects['incorrects'],
                         'quests_cache': quests_from_get,
                         'questions_count': quests_from_get['count'],
                         }
                )


def get_quests_cached(request):
    try:
        uid = request.session['question_session_id']
        qfg = cache.get(uid)
        cache.delete(uid)
        del request.session['question_session_id']
        return qfg
    except KeyError:
        raise TimeoutError('Timeout! Get out!')


def compare_answers(questions, raw_dict):
    corrects_count = 0
    incorrects = []
    corrects = get_corrects(questions)
    for key in corrects:
        if set(corrects[key]) == set(raw_dict[key]):
            corrects_count += 1
        else:
            incorrects.append(get_object_or_404(Question, id=key))

    return {'corrects_count': corrects_count,
            'incorrects': incorrects,
            }


def get_corrects(question_list):
    corrects = dict()
    for question_id in question_list:
        question = Question.objects.get(id=question_id)
        tmp_corrects = list()
        for answer in question.answer_set.all():
            if answer.correct:
                tmp_corrects.append(answer.id)
            corrects[question_id] = tmp_corrects
    print(f"CORRECTS!! {corrects}")
    return corrects
