from django.shortcuts import render
from rest_framework import generics
from sentiment.models import TwitterSentiment 
from serializer import TwitterSentimentSerializer

class TwitterSentimentList(generics.ListCreateAPIView):
    queryset = TwitterSentiment.objects.all()
    serializer_class = TwitterSentimentSerializer
