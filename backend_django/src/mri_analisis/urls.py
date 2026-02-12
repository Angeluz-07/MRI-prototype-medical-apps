from django.urls import path

from .views import ListAlgorithm, DetailAlgorithm

urlpatterns = [
    path('<int:pk>/', DetailAlgorithm.as_view()),
    path('', ListAlgorithm.as_view()),
]
