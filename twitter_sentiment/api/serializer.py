from rest_framework import serializers
from sentiment.models import TwitterSentiment

class TwitterSentimentSerializer(serializers.ModelSerializer):
	class Meta:
		model=TwitterSentiment
		fields='__all__'


