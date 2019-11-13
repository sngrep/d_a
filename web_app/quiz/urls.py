from django.urls import path
from .views import ChooseCollectionView, QuizStartView, QuizResultsDetail, get_selected_choices, get_raw_answers

app_name = 'quiz'

urlpatterns = [
    path('qc/', ChooseCollectionView.as_view(), name='choose_collection'),
    path('test/<int:pk>/', QuizStartView.as_view(), name='quiz_start'),
    path('results/<int:pk>/', QuizResultsDetail.as_view(), name='quiz_results'),
    path('test/test/', get_raw_answers, name='get_raw_answers'),
    path('<int:question_id>/vote/', get_selected_choices, name='get_selected_choices'),
]
