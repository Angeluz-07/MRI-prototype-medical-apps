from django.shortcuts import render
from rest_framework import generics
from .models import Algorithm, User
from .serializers import AlgorithmSerializer, UserSerializer

class ListAlgorithm(generics.ListAPIView):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer

class DetailAlgorithm(generics.RetrieveAPIView):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        # Always returns the user tied to the Token/Session
        return self.request.user