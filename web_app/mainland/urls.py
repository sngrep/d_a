from django.urls import path
from .views import (
                QcollectionListView,
                QcollectionCreateView,
                QuestionCreateView,
                QuestionListView,
                QuestionDetailView,
                )

app_name = 'mainland'

urlpatterns = [
    path('collection/', QcollectionListView.as_view(), name='qc_list'),
    path(
        'collection/create/',
        QcollectionCreateView.as_view(),
        name='qc_create'
        ),
    path(
        'create/',
        QuestionCreateView.as_view(),
        name='q_create'
        ),
    path('list/', QuestionListView.as_view(), name='q_list'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='q_detail'),
]
