from django.conf.urls import url
from views import *

urlpatterns=[
	url(r'^twiiter_sentiment_list/$',TwitterSentimentList.as_view()),
]