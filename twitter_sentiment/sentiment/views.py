from django.shortcuts import render
from utility import TwitterClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

api = TwitterClient('@ritu')


# utility function
def utility(v):
    if v!=None:
        return v in ["yes", "true", "t", "1"]

def home(request):
    return render(request,'home.html',{})


@csrf_exempt
def tweets(request):
    print 'inside tweeting'
    retweets_only = request.POST.get('retweets_only')
    ## for debugging
    print retweets_only
    print '############'

    api.set_retweet_checking(utility(retweets_only))
    # getting sentiment
    with_sentiment = request.POST.get('with_sentiment')
    api.set_with_sentiment(utility(with_sentiment))
    # getting seach query 
    query = request.POST.get('query')
    api.set_query(query)

    # getting tweets related to query
    positive_sentiment=0
    negative_sentiment=0
    neutral_sentiment=0
    tweets = api.get_tweets()
    # for tweet in tweets:
    #     if tweet['sentiment']=='positive':
    #         positive_sentiment+=1
    #     elif tweet['sentiment']=='negative':
    #         negative_sentiment+=1
    #     else:
    #         neutral_sentiment+=1        
            
    ## for debugging
    print positive_sentiment,negative_sentiment,neutral_sentiment
    print type(tweets)

    return JsonResponse({'data': tweets, 'count': len(tweets)})
