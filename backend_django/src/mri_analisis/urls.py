from django.urls import path

from .views import ListAlgorithm, DetailAlgorithm, UserDetailView

urlpatterns = [
    path('me/', UserDetailView.as_view()),
    path('algorithms/<int:pk>/', DetailAlgorithm.as_view()),
    path('algorithms/', ListAlgorithm.as_view()),
]
