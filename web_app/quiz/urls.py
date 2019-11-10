from django.urls import path
from .views import QuizStartView, QuizResultsDetail, get_selected_choices

app_name = 'quiz'

urlpatterns = [
    path('test/', QuizStartView.as_view(), name='quiz_start'),
    path('results/<int:pk>/', QuizResultsDetail.as_view(), name='quiz_results'),
    path('<int:question_id>/vote/', get_selected_choices, name='get_selected_choices'),
]
