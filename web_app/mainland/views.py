from django.views.generic import (
                                 CreateView,
                                 ListView,
                                 DetailView,
                                 DeleteView,
                                 TemplateView
                                 )
from .models import QCollection, Question, Answer


class QcollectionCreateView(CreateView):
    model = QCollection
    template_name = 'mainland/qcollection_create.html'
    fields = ['name', 'amount_of_questions_per_session']


class QcollectionListView(ListView):
    model = QCollection
    queryset = QCollection.objects.all()
    paginate_by = 10


class QuestionCreateView(CreateView):
    model = Question
    template_name = 'mainland/question_create.html'
    fields = ['question', 'related_qcollection']


class QuestionListView(ListView):
    queryset = Question.objects.filter(related_qcollection=1)
    model = Question
    paginate_by = 10


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['answer_list'] = Answer.objects.filter(related_question=self.kwargs['pk'])

        return context


class QuestionDeleteView(DeleteView):
    model = Question


class HomeView(TemplateView):
    template_name = 'mainland/home_view.html'


class AboutView(TemplateView):
    template_name = 'mainland/about_view.html'